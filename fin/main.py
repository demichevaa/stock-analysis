import json
import boto3
from datetime import datetime

s3 = boto3.client("s3")

raw = {
    "bucket": "daa-fin",
    "schema": "raw",
    "partitions": ["source", "endpoint", "year", "month", "day"],
}


def put(s3_context, obj: any, fmt="json"):
    bucket = s3_context["bucket"]
    schema = s3_context["schema"]
    partitions = s3_context["partitions"]

    now = datetime.utcnow()
    key_prefix = f"{schema}/exchanges/{now.year}/{now.month:02}/{now.day:02}"

    if fmt == "json":
        content = json.dumps(obj, indent=2)
        key = f"{key_prefix}/data.json"
    elif fmt == "csv":
        headers = obj[0].keys() if obj else []
        content = "\n".join([",".join(headers)] + [",".join(map(str, row.values())) for row in obj])
        key = f"{key_prefix}/data.csv"
    else:
        raise ValueError("Unsupported format")

    s3.put_object(Bucket=bucket, Key=key, Body=content)
    print(f"Uploaded to s3://{bucket}/{key}")


def lambda_handler(event, context) -> dict:
    exchanges = eodhd.call("exchanges-list")
    put(raw, exchanges, fmt="json")  # Change fmt to "csv" if needed
    return {"status": "success"}


if __name__ == "__main__":
    lambda_handler(None, None)
