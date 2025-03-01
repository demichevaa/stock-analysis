from functools import cached_property
from os import path, environ

from dtk.utils.singleton import singleton
from utils.logger import get_logger

from dtk.
from dtk_lib

@singleton
class ApplicationContext:
    def on_create(self, *args, **kwargs):
        logger = get_logger(__name__)
        logger.info(f"Initializing project context for `{self.project_root_path}`.")
        try:
            from dotenv import load_dotenv
            load_dotenv()
        except ModuleNotFoundError as e:

            logger.warning("`.env` file is ignored due to the `python-dotenv`package not being found.")

    @cached_property
    def project_root_path(self) -> str:
        return path.abspath(path.join(path.dirname(__file__), "..", ".."))

    @cached_property
    def local_file_storage_path(self) -> str:
        return environ.get(
            "LOCAL_FILE_STORAGE_PATH",
            path.join(self.project_root_path, "data/")
        )


    @cached_property
    def alpha_vantage_api_key(self) -> str:
        return get_venv_or_raise("ALPHA_VANTAGE_API_KEY")

    @cached_property
    def eodhd_api_key(self) -> str:
        return get_venv_or_raise("EODHD_API_KEY")