import datetime
import json
from typing import NamedTuple, Type
from exceptions import CanNotReedJsons


class DictsData(NamedTuple):
    dict1: dict
    dict2: dict | None


class Settings(NamedTuple):
    product_type: str
    account_number: str
    contact_id: str
    is_date_format: bool
    is_format_contract: bool
    is_format_primary_account_number: bool


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
            answer = fill_dict_from_anouther_dict(from_fill_dict, to_fill_dict, settings)
        except json.decoder.JSONDecodeError:
            return "Невалидный JSON from fill"

    return str(answer)


def fill_dict_from_anouther_dict(from_fill: dict, to_dill: dict, settings: Settings) -> dict:
    pass


def fill_dict_from_root_json(to_fill: dict, settings: Settings) -> dict:
    is_custom_product_type: bool
    is_custom_contact_id: bool
    is_custom_account_number: bool
    result_dict = {}

    with open("data/root_json_from_fill.json", "r", encoding="UTF-8") as file:
        from_fill: dict = json.load(file)

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

    for k, v in from_fill.items():

        if k in to_fill:

            if (k == "ACCOUNT_NUMBER") and is_custom_account_number:
                result_dict[k] = settings.account_number
                continue

            elif (k == "CONTACT_ID") and is_custom_contact_id:
                result_dict[k] = settings.contact_id
                continue

            elif k == "PRODUCT_TYPE":
                if is_custom_product_type:
                    result_dict[k] = settings.product_type
                elif settings.product_type == "Кредитная карта":
                    result_dict[k] = 'Common'
                elif settings.product_type == "КВК\\КН":
                    result_dict[k] = "Kvk"
                else:
                    result_dict[k] = v

            elif (k == "PRIMARY_ACCOUNT_NUMBER") and settings.is_format_primary_account_number:
                result_dict[k] = settings.account_number
                continue

            elif (k == "PRIMARY_CONTRACT_NUMBER" or k == "CONTRACT_NUMBER") and settings.is_format_contract:
                result_dict[k] = settings.account_number
                continue

            # TODO: Data&Time Доделать валидацию
            else:
                result_dict[k] = v
        else:
            pass

    return result_dict
