from typing import TypeVar

import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout

from connectors.http.exceptions import HTTPConnectorException, HTTPConnectorHTTPError, HTTPConnectorTimeoutError, \
    HTTPResponseConverterError
from utils.logger import get_logger

LOGGER = get_logger(__name__)

T = TypeVar("T")


def get(
    base_url: str,
    query_params: dict = None,
    headers: dict = None,
    timeout: int = 10,
    request_params: dict = None,
    # response_converter: Callable[[Response], T] = json_response_to_dict
) -> T:
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
            headers=headers or {},
            timeout=timeout,
        )

        r.raise_for_status()

        parsed_response = lambda x: x.content
        LOGGER.info(f"Get request to `{base_url}` finished successfully", **context)

        return parsed_response

    # TODO: Messy exception handling. Revisit after structure logging impl
    except HTTPError as http_err:
        http_status = str(http_err.args[0])
        LOGGER.error(f"HTTP error occurred [{http_status}]: {http_err}", http_status=http_status, **context)
        raise HTTPConnectorHTTPError
    except Timeout as timeout_err:
        LOGGER.error(f"Timeout error occurred: {timeout_err}", **context)
        raise HTTPConnectorTimeoutError
    except ConnectionError as conn_err:
        LOGGER.error(f"Connection error occurred: {conn_err}", **context)
        raise HTTPConnectorException
    except HTTPResponseConverterError as e:
        LOGGER.error(f"Connection error occurred: {e}", **context)
        raise HTTPConnectorException
    except Exception as err:
        LOGGER.critical(f"Unexpected error: {err}")
        raise HTTPConnectorException(f"Unexpected error: {err}")
