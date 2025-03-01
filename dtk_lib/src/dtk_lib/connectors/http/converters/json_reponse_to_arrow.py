import pyarrow as pa
from pyarrow import Table, ArrowException
from requests import Response

from connectors.http.exceptions import HTTPResponseConverterError
from utils.logger import get_logger

LOGGER = get_logger(__name__)


def json_response_to_arrow(response: Response) -> Table:
    try:
        data = response.json()

        columns = data[0].keys()
        columnar_data = [[item[col] for item in data] for col in columns]
        table = pa.table(dict(zip(columns, columnar_data)))

        LOGGER.info("Response decoded to arrow successfully", schema=table.schema)
        return table

    except ArrowException as e:
        raise HTTPResponseConverterError(f"Failed to convert json response to arrow table: {e}")