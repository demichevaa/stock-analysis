# https://www.alphavantage.co/documentation/
from pyarrow import Table

from dtk.common.project_context import ProjectContext
from dtk.connectors.http import connector as http
from dtk.connectors.http.converters.csv_response_to_arrow import csv_response_to_arrow
from dtk.connectors.http.exceptions import HTTPConnectorException
from dtk.utils.logger import get_logger

LOGGER = get_logger(__name__)

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = ProjectContext().alpha_vantage_api_key


def call(function: str, **kwargs) -> Table:
    """
    Call a remote function on the Alpha Vantage API.

    This function requires the environment variable `ALPHA_VANTAGE_API_KEY` to be set.
    It sends a GET request to the Alpha Vantage API using the specified function name
    and any additional query parameters provided as keyword arguments.

    Args:
        function (str): The name of the Alpha Vantage function to call (e.g., 'TIME_SERIES_MONTHLY').
        **kwargs: Additional query parameters supported by the specified function,
                  such as `symbol="IBM"`.

    Returns:
        dict: The JSON response from the Alpha Vantage API.

    Exits:
        Exits the program with status code 1 if an HTTPConnectorException occurs.
    """

    params = {
        "apikey": API_KEY,
        "function": function,
        "datatype": "csv",
        **kwargs
    }

    LOGGER.info(f"Calling function `{function}` via alphavantage api", **params)
    try:
        return http.get(
            BASE_URL,
            query_params=params,
            response_converter=csv_response_to_arrow
        )
    except HTTPConnectorException as e:
        LOGGER.critical(f"Failed function call `{function}` via alphavantage api: {e}", **params)
        import sys
        sys.exit(1)


def get_time_series_monthly(symbol: str) -> Table:
    return call("TIME_SERIES_MONTHLY", symbol=symbol)

