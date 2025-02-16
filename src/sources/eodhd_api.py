# https://eodhd.com/financial-apis/python-financial-libraries-and-code-samples
from functools import lru_cache

from eodhd import APIClient

from common.project_context import ProjectContext
from utils.logger import get_logger

LOGGER = get_logger(__name__)
API_KEY = ProjectContext().eodhd_api_key

@lru_cache(maxsize=None)
def api() -> APIClient:
    LOGGER.info("Creating eodhd api client.")
    return APIClient(API_KEY)
