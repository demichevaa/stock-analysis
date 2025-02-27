import io

import pyarrow.csv as pa
from pyarrow import Table, ArrowException
from requests import Response

from dtk.connectors.http.exceptions import HTTPResponseConverterError
from dtk.utils.logger import get_logger

LOGGER = get_logger(__name__)



def csv_response_to_arrow(response: Response) -> Table:
    try:
        csv_buffer = io.BytesIO(response.content)
        table = pa.read_csv(csv_buffer)

        LOGGER.debug("Response decoded to arrow successfully.", schema=table.schema)
        return table

    except ArrowException as e:
        raise HTTPResponseConverterError(f"Failed to convert csv response to arrow table: {e}")
