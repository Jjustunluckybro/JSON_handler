import json

from utils.DataTypes import Settings, MappedSettings


def filler(
        to_fill_str: str,
        from_fill_str: str,
        settings: Settings
) -> str:
    if to_fill_str == "\n":
        return "Поле 'JSON to fill' должно быть обязательно заполнено"

    try:
        to_fill_dict: dict = json.loads(to_fill_str)
    except json.decoder.JSONDecodeError:
        return "Невалидный JSON to fill"

    if from_fill_str == "\n":
        answer = fill_dict_from_root_json(to_fill_dict, settings)
    else:
        try:
            from_fill_dict: dict = json.loads(from_fill_str)
            answer = fill_dict_from_another_dict(from_fill_dict, to_fill_dict, settings)
        except json.decoder.JSONDecodeError:
            return "Невалидный JSON from fill"

    return correct_dict_to_export(answer)


def fill_dict_from_another_dict(from_fill: dict, to_fill: dict, settings: Settings) -> dict:
    result_dict = {}

    # Маппим настройки кастомных данных
    custom_mapped_settings = mapping_custom_settings(settings=settings)

    # Переносим все ключи\значения, которых нет в from_fill
    result_dict = fill_keys_not_in_from_fill(
        dict_to_fill_result=result_dict,
        to_fill=to_fill,
        from_fill=from_fill
    )

    # Переносим все значения по совпадающим ключам из from_fill в to_fill
    result_dict = fill_values_by_keys(
        dict_to_fill_result=result_dict,
        from_fill=from_fill,
        to_fill=to_fill,
        is_custom_account_number=custom_mapped_settings.is_custom_account_number,
        is_custom_contact_id=custom_mapped_settings.is_custom_contact_id,
        settings=settings
    )

    # Проверяем и переносим значение account_number
    result_dict = check_and_fill_primary_account_number_key(
        dict_to_fill_result=result_dict,
        to_fill=to_fill,
        from_fill=from_fill,
        settings=settings,
        is_custom_account_number=custom_mapped_settings.is_custom_account_number
    )

    # Проверяем и переносим знaчения primary contract_number
    result_dict = check_and_fill_primary_contract_keys(
        dict_to_fill_result=result_dict,
        from_fill=from_fill,
        to_fill=to_fill,
        is_custom_account_number=custom_mapped_settings.is_custom_account_number,
        settings=settings
    )

    # Проверяем и переносим знaчения contract_number
    result_dict = check_and_fill_contract_keys(
        dict_to_fill_result=result_dict,
        from_fill=from_fill,
        to_fill=to_fill,
        is_custom_account_number=custom_mapped_settings.is_custom_account_number,
        settings=settings
    )

    # проверяем и заполняем поле product_type в зависимости от настроек
    result_dict = check_and_fill_product_type(
        dict_to_fill_result=result_dict,
        settings=settings,
        is_custom_product_type=custom_mapped_settings.is_custom_product_type
    )

    # Проверяем и заполняем значение communication_type
    result_dict = check_and_fill_communication_type(
        dict_to_fill_result=result_dict,
        settings=settings
    )

    if settings.is_date_format:
        result_dict = check_and_fix_all_dt(result_dict)

    return result_dict


def fill_dict_from_root_json(to_fill: dict, settings: Settings) -> dict:

    with open("data/root_json_from_fill.json", "r", encoding="UTF-8") as file:
        from_fill: dict = json.load(file)

    result_dict = fill_dict_from_another_dict(from_fill=from_fill, to_fill=to_fill, settings=settings)
    return result_dict


# TODO: Need to refactor with regular exp
def is_it_data_time(string: str) -> bool:
    """Check string to dt pattern"""
    num_of_colon = 0
    num_of_t = 0
    num_of_hyphen = 0

    if type(string) is not str:
        return False

    for i in string:
        if i == ":":
            num_of_colon += 1
        elif i == "-":
            num_of_hyphen += 1
        elif i == "T" or i == "Т":
            num_of_t += 1

    if num_of_t == 1 and num_of_colon == 2 and num_of_hyphen == 2:
        return True
    else:
        return False


def dt_to_data(dt: str) -> str:
    """
    2022-06-17T00:00:00
    2022-11-28T08:25:47.989
    """
    data = dt[0:10]
    return data


def mapping_product_type(settings: Settings, is_custom_product_type: bool) -> str:
    """
    Возвращает значение ключа product_type в зависимости от настроек
    """
    if is_custom_product_type:
        return settings.product_type
    elif settings.product_type == "Кредитная карта":
        return 'Common'
    elif settings.product_type == "КВК\\КН":
        return "Kvk"
    else:
        return "Skip"


def mapping_communication_type(settings: Settings) -> str:
    """
    Возвращает значение ключа COMMUNICATION_TYPE в зависимости от настроек
    """

    if settings.communication_type == "Звонок":
        return "Call"
    elif settings.communication_type == "Чат":
        return "Chat"
    else:
        return "Skip"


def fill_values_by_keys(
        dict_to_fill_result: dict,
        from_fill: dict,
        to_fill: dict,
        is_custom_account_number: bool,
        is_custom_contact_id: bool,
        settings: Settings
) -> dict:
    for k, v in from_fill.items():

        if k in to_fill:

            if(k == "CONTACT_ID") and is_custom_contact_id:
                dict_to_fill_result[k] = settings.contact_id
                continue

            else:
                dict_to_fill_result[k] = v

    return dict_to_fill_result


def check_and_fill_primary_contract_keys(
        dict_to_fill_result: dict,
        to_fill: dict,
        from_fill: dict,
        settings: Settings,
        is_custom_account_number: bool
) -> dict:

    # Проверяем и переносим знaчения Primary Contract Number
    if "PRIMARY_CONTRACT_NUMBER" in to_fill.keys():

        if settings.is_format_contract:
            if is_custom_account_number:
                dict_to_fill_result["PRIMARY_CONTRACT_NUMBER"] = settings.account_number
                return dict_to_fill_result
        else:
            if "PRIMARY_CONTRACT_NUMBER" in from_fill.keys():
                dict_to_fill_result["PRIMARY_CONTRACT_NUMBER"] = from_fill["PRIMARY_CONTRACT_NUMBER"]
                return dict_to_fill_result
            else:
                dict_to_fill_result["PRIMARY_CONTRACT_NUMBER"] = to_fill["PRIMARY_CONTRACT_NUMBER"]
                return dict_to_fill_result
    return dict_to_fill_result


def check_and_fill_contract_keys(
        dict_to_fill_result: dict,
        to_fill: dict,
        from_fill: dict,
        settings: Settings,
        is_custom_account_number: bool
) -> dict:

    # Проверяем и переносим знaчения Primary Contract Number
    if "CONTRACT_NUMBER" in to_fill.keys():

        if settings.is_format_contract:
            if is_custom_account_number:
                dict_to_fill_result["CONTRACT_NUMBER"] = settings.account_number
                return dict_to_fill_result
        else:
            if "CONTRACT_NUMBER" in from_fill.keys():
                dict_to_fill_result["CONTRACT_NUMBER"] = from_fill["CONTRACT_NUMBER"]
                return dict_to_fill_result
            else:
                dict_to_fill_result["CONTRACT_NUMBER"] = to_fill["CONTRACT_NUMBER"]
                return dict_to_fill_result
    return dict_to_fill_result


def check_and_fill_primary_account_number_key(
        dict_to_fill_result: dict,
        to_fill: dict,
        from_fill: dict,
        settings: Settings,
        is_custom_account_number: bool
) -> dict:

    if "ACCOUNT_NUMBER" in dict_to_fill_result:
        if is_custom_account_number:
            dict_to_fill_result["ACCOUNT_NUMBER"] = settings.account_number

    if "PRIMARY_ACCOUNT_NUMBER" in dict_to_fill_result:
        if settings.is_format_primary_account_number:
            if is_custom_account_number:
                dict_to_fill_result["PRIMARY_ACCOUNT_NUMBER"] = settings.account_number
                return dict_to_fill_result
        else:
            if "PRIMARY_ACCOUNT_NUMBER" in from_fill.keys():
                dict_to_fill_result["PRIMARY_ACCOUNT_NUMBER"] = from_fill["PRIMARY_ACCOUNT_NUMBER"]
                return dict_to_fill_result
            else:
                dict_to_fill_result["PRIMARY_ACCOUNT_NUMBER"] = to_fill["PRIMARY_ACCOUNT_NUMBER"]
                return dict_to_fill_result

    return dict_to_fill_result


def check_and_fill_product_type(
        dict_to_fill_result: dict,
        settings: Settings,
        is_custom_product_type: bool
) -> dict:

    product_type = mapping_product_type(
        settings=settings,
        is_custom_product_type=is_custom_product_type
    )
    if product_type == "Skip":
        return dict_to_fill_result
    else:
        probably_keys = ("PRODUCT_TYPE", "PRIMARY_ACCOUNT_PRODUCT_TYPE", "SECONDARY_ACCOUNT_PRODUCT_TYPE")

        for key in probably_keys:
            if key in dict_to_fill_result:
                dict_to_fill_result[key] = product_type

        return dict_to_fill_result


def fill_keys_not_in_from_fill(
        dict_to_fill_result: dict,
        to_fill: dict,
        from_fill: dict,
) -> dict:

    for k, v in to_fill.items():
        if k not in from_fill.keys():
            dict_to_fill_result[k] = v

    return dict_to_fill_result


def check_and_fill_communication_type(
        dict_to_fill_result: dict,
        settings: Settings
) -> dict:

    communication_type = mapping_communication_type(settings=settings)

    if "COMMUNICATION_TYPE" not in dict_to_fill_result.keys() or communication_type == "Skip":
        return dict_to_fill_result
    else:
        dict_to_fill_result['COMMUNICATION_TYPE'] = communication_type
        return dict_to_fill_result


def correct_dict_to_export(correcting_dict: dict) -> str:
    correcting_value = str(correcting_dict)
    correcting_value = correcting_value.replace("'", '"')
    correcting_value = correcting_value.replace("True", 'true')
    correcting_value = correcting_value.replace("False", 'false')
    correcting_value = correcting_value.replace("None", 'null')
    correcting_value = correcting_value.replace(",", ',\n')

    return correcting_value


def mapping_custom_settings(settings: Settings) -> MappedSettings:

    if settings.product_type == "Взять_из_исходного_JSON'a" \
            or settings.product_type == "Кредитная карта" \
            or settings.product_type == "КВК\\КН":
        is_custom_product_type = False
    else:
        is_custom_product_type = True

    if settings.contact_id == "Взять_из_исходного_JSON'a":
        is_custom_contact_id = False
    else:
        is_custom_contact_id = True

    if settings.account_number == "Взять_из_исходного_JSON'a":
        is_custom_account_number = False
    else:
        is_custom_account_number = True

    mapped_settings = MappedSettings(
        is_custom_account_number=is_custom_account_number,
        is_custom_contact_id=is_custom_contact_id,
        is_custom_product_type=is_custom_product_type,
    )

    return mapped_settings


def check_and_fix_all_dt(
        dict_to_fill_result: dict
) -> dict:

    for key, value in dict_to_fill_result.items():
        if is_it_data_time(value):
            dict_to_fill_result[key] = dt_to_data(value)

    return dict_to_fill_result
