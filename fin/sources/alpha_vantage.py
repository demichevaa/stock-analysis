# https://www.alphavantage.co/documentation/
from dtk.connectors.http.exceptions import HTTPConnectorException

# from dtk-core-core.connectors.http.typing import Response
# from common.project_context import ProjectContext
# from connectors.http import connector as http
# from connectors.http.exceptions import HTTPConnectorException
# from utils.logger import get_logger
# import dtk-core-core
LOGGER = get_logger(__name__)

BASE_URL = "https://www.alphavantage.co/query"
API_KEY = ProjectContext().alpha_vantage_api_key


def call(function: str, **kwargs) -> Response:
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
        content = http.get(
            BASE_URL,
            query_params=params,
            #response_converter=csv_response_to_arrow
        )
        return Response(content_type="csv", content=content)
    except HTTPConnectorException as e:
        LOGGER.critical(f"Failed function call `{function}` via alphavantage api: {e}", **params)
        import sys
        sys.exit(1)


def get_time_series_monthly(symbol: str) -> Response:
    return call("TIME_SERIES_MONTHLY", symbol=symbol)

