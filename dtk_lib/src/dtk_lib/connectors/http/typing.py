import dataclasses
from io import BytesIO
from typing import Literal


@dataclasses.dataclass
class Response:
    content_type: Literal["json", "csv", "xml", "parquet"]
    content: BytesIO
