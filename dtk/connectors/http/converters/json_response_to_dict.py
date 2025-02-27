from json import JSONDecodeError

from requests import Response

from dtk.connectors.http.exceptions import HTTPResponseConverterError
from dtk.utils.logger import get_logger

LOGGER = get_logger(__name__)


def json_response_to_dict(response: Response) -> dict:
    try:
        decoded = response.json()

        LOGGER.debug("Response decoded as JSON successfully.")
        return decoded
    except (JSONDecodeError, ValueError) as e:
        raise HTTPResponseConverterError(f"Failed to convert response to JSON object: {e}")
