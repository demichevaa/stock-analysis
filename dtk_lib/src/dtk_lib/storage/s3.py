from functools import cached_property
from typing import List

import boto3


class S3:
    def __init__(self, bucket: str, region: str, partitions: List[str]):
        self.bucket = bucket
        self.region = region
        self.partitions = partitions

    @cached_property
    def _client(self) -> boto3.client:
        return boto3.client("s3", region_name=self.region)

    def put(self, ):
        self._client

    def get(self):
        pass


S3().put()