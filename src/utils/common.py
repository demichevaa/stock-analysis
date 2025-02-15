import datetime


def get_current_timestamp() -> int:
    return round(datetime.datetime.now().timestamp())
