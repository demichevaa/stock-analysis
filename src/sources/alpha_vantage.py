from src.common.project_context import ProjectContext
from src.connectors import http
from src.connectors.http import HTTPConnectorException
from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = ProjectContext().alpha_vantage_api_key


def call_function(function: str, **kwargs) -> dict:
    params = {
        "apikey": API_KEY,
        "function": function,
        "datatype": "json",
        **kwargs
    }

    LOGGER.info(f"Calling function `{function}` via alphavantage api", **params)
    try:
        return http.get(BASE_URL, query_params=params)
    except HTTPConnectorException as e:
        LOGGER.critical(f"Failed function call `{function}` via alphavantage api", **params)
        import sys
        sys.exit(1)


def get_time_series_monthly(symbol: str):
    return call_function("TIME_SERIES_MONTHLY", symbol=symbol)
