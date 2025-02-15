import datetime
from typing import Any, Hashable, Optional


def get_current_timestamp() -> int:
    return round(datetime.datetime.now().timestamp())

def dict_set_optional(target: dict, key: Hashable, value: Optional[Any]) -> dict:
    """
    :param target: dict to add k: v
    :param key: key
    :param value: value with possible None
    :return:
    """
    target |= {key: value} if value else {}

    return target

def dict_merge_optional(target)