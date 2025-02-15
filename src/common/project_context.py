from functools import cached_property
from os import environ

from src.utils.singleton import singleton


class ProjectContextException(Exception):
    pass


def get_venv_or_raise(key: str) -> str:
    if value := environ.get(key):
        return value
    raise ProjectContextException(f"{key} is not found in venv.")


@singleton
class ProjectContext:
    def on_create(self, *args, **kwargs):
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ModuleNotFoundError as e:
            from src.utils.logger import get_logger
            get_logger(__name__).warning("`.env` file is ignored due to the `python-dotenv`package not being found.")

    @cached_property
    def alpha_vantage_api_key(self) -> str:
        return get_venv_or_raise("ALPHA_VANTAGE_API_KEY")
