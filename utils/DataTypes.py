from typing import NamedTuple


class BoxesResolution(NamedTuple):
    height: int
    width: int


class DictsData(NamedTuple):
    dict1: dict
    dict2: dict | None


class MappedSettings(NamedTuple):
    is_custom_product_type: bool
    is_custom_contact_id: bool
    is_custom_account_number: bool


class Settings(NamedTuple):
    product_type: str
    account_number: str
    contact_id: str
    communication_type: str
    is_date_format: bool
    is_format_contract: bool
    is_format_primary_account_number: bool
