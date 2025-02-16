import pyarrow.parquet as pq
from pyarrow import Table, ArrowException
from pyarrow import fs

from utils.common import create_dir_if_not_exists
from utils.logger import get_logger

LOGGER = get_logger(__name__)



def local_write(table: Table, path_to_file: str) -> None:
    try:
        create_dir_if_not_exists(path_to_file)
        local = fs.LocalFileSystem()

        with local.open_output_stream(path_to_file) as out:
            pq.write_table(table, out)
        LOGGER.info(f"Successfully wrote Parquet file to `{path_to_file}`")

    except (OSError, ArrowException) as e:
        LOGGER.error(f"Failed to write Arrow Table to Parquet at `{path_to_file}`: {e}")
        raise
    except Exception as e:
        LOGGER.error(f"Unexpected error occurred while writing to `{path_to_file}`: {e}")
        raise

# get_storage("LOCAL").save(file, "/opt/example.csv")
# from_local = get_storage("LOCAL").load("/opt/example.csv")
#
# get_storage("S3").save(file, "bucket1", "path/to/your-object.txt")
# from_s3 = get_storage("S3").load("bucket1", "path/to/your-object.txt")

# with open(f"{ProjectContext().local_file_storage_path}/123", "r") as f:
#     local_save(f, f"{ProjectContext().local_file_storage_path}/123_new")


# class SerializationError(Exception):
#     pass
#
# def serialize_json(raw: Any, path_to_file: str, *_, **kwargs) -> None:
#     import json
#
#     try:
#         with open(path_to_file, "w") as f:
#             json.dump(
#                 raw,
#                 fp=cast(SupportsWrite[str], f),
#                 **kwargs
#             )
#             LOGGER.info(f"Serialized to `{path_to_file}`.")
#     except (FileNotFoundError, PermissionError, OSError, IOError) as e:
#         raise SerializationError(f"Error writing to file `{path_to_file}`: {e}")
#     except TypeError as e:
#         raise SerializationError(f"Unable to serialize the object with json: {e}")
#
#
# def serialize_pickle(raw: Any, path_to_file: str) -> None:
#     import pickle
#
#     try:
#         with open(path_to_file, "wb") as f:
#             pickle.dump(raw, f)
#             LOGGER.info(f"Serialized to `{path_to_file}`.")
#     except (FileNotFoundError, PermissionError, OSError, IOError) as e:
#         raise SerializationError(f"Error writing to file `{path_to_file}`: {e}")
#     except Exception as e:
#         raise SerializationError(f"Unable to serialize pickle the object with pickle: {e}")
#
#
# def serialize_parquet(raw: Any, path_to_file: str) -> None:
#     try:
#         import pyarrow as pa
#         import pyarrow.parquet as pq
#
#         if not isinstance(raw, (pd.DataFrame, list)):
#             raise SerializationError(
#                 f"Unsupported data type: {type(raw).__name__}. Expected pandas.DataFrame, dict, or list.")
#
#
#     except ModuleNotFoundError as e:
#         LOGGER.critical("Module `pandas` is required for serialization: `pip install pandas`")
#     except Exception as e:
#         LOGGER.error(f"Unable to serialize the object: {e}")

# def serialize(raw: Any, serializer) -> str:
