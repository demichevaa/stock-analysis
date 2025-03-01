# https://eodhd.com/financial-apis/python-financial-libraries-and-code-samples

# from connectors.http.typing import Response
# from common.project_context import ProjectContext
# from connectors.http import connector as http
# from connectors.http.exceptions import HTTPConnectorException
# from utils.logger import get_logger

LOGGER = get_logger(__name__)
API_KEY = ProjectContext().eodhd_api_key
BASE_URL = "https://eodhd.com/api/"

def call(endpoint: str, **kwargs) -> Response:
    params = {
        "api_token": API_KEY,
        "fmt": "json",
        **kwargs
    }

    LOGGER.info(f"Calling endpoint `{endpoint}` via eodhd api", **params)
    try:
        content =  http.get(
            BASE_URL + '/' + endpoint,
            query_params=params,
            #response_converter=json_response_to_arrow
        )

        return Response(content_type="json", content=content)
    except HTTPConnectorException as e:
        LOGGER.critical(f"Failed endpoint call `{endpoint}` via eodhd api: {e}", **params)
        import sys
        sys.exit(1)


def get_exchange_list() -> Response:
    return call("exchanges-list")

if __name__ == "__main__":
    from storage.local import local_write

    res = get_exchange_list()
    local_write(res, ProjectContext().local_file_storage_path + "eeod__exchanges_list.parquet")
