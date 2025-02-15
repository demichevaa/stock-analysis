import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

class HTTPConnectorException(Exception):
    pass

class HTTPConnectorHTTPError(HTTPConnectorException):
    pass

class HTTPConnectorTimeoutError(HTTPConnectorException):
    pass


def get(
        base_url: str,
        query_params: dict = None,
        headers: dict = None,
        timeout: int = 10,
        request_params: dict = None
) -> dict:
    context = dict(
        base_url=base_url,
        query_params=query_params,
        headers=headers,
        timeout=timeout,
        request_params=request_params
    )

    try:
        LOGGER.info(f"Initializing get request to `{base_url}`", **context)

        r = requests.get(
            base_url,
            params=query_params,
            **request_params or {},
            headers = headers or {},
            timeout=timeout,
        )

        r.raise_for_status()

        LOGGER.info(f"Get request to `{base_url}` finished successfully", **context)
        return r.json()
    except HTTPError as http_err:
        http_status = http_err.args[0]
        LOGGER.error(f"HTTP error occurred [{str(http_status)}]: {http_err}", http_status=http_status, **context)
        raise HTTPConnectorHTTPError
    except Timeout as timeout_err:
        LOGGER.error(f"Timeout error occurred: {timeout_err}", **context)
        raise HTTPConnectorTimeoutError
    except ConnectionError as conn_err:
        LOGGER.error(f"Connection error occurred: {conn_err}", **context)
        raise HTTPConnectorException
    except Exception as err:
        LOGGER.critical(f"Unexpected error: {err}")
        raise HTTPConnectorException(f"Unexpected error: {err}")
