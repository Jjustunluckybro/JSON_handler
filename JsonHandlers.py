import json
from typing import NamedTuple, Type
from exceptions import CanNotReedJsons


class DictsData(NamedTuple):
    dict1: dict
    dict2: dict | None


def filler(
        to_fill_str: str,
        from_fill_str: str,
        product_type: str | None,
        is_fill_primary_contract_number: bool,
        is_fill_primary_account_number: bool,
        is_format_dt: bool,
) -> str:

    # dicts = convert_string_to_dict(str1, str2)

    # answer = fill_json(jsons)
    # return answer
    pass

def convert_string_to_dict(str1: str = None, str2: str = None) -> Type[DictsData]:
    """
    Convert two strings in dicts and return DictData
    """
    answer = DictsData
    try:
        json_1: dict = json.loads(str1)
        answer.dict1 = json_1
        if str2 != "\n":
            json_2: dict = json.loads(str2)
            answer.dict2 = json_2
            return answer
        else:
            answer.dict2 = None
            return answer
    except json.decoder.JSONDecodeError:
        raise CanNotReedJsons


def fill_json(jsons: Type[DictsData]) -> str:
    if jsons.dict2 is None:
        return fill_from_base_json(jsons.dict1)
    else:
        return fill_from_another_json(jsons)


def fill_from_base_json(to_fill: dict) -> str:
    with open("data/root_json_to_fill.json", "r") as file:
        root_json = json.load(file)






def fill_from_another_json(jsons: Type[DictsData]) -> str:
    pass

convert_string_to_dict('123', '123')