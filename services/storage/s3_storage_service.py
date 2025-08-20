import boto3
import tempfile
import os

import settings
from services.storage.istorage_service import IStorageService


class S3StorageService(IStorageService):

    def __init__(self):
        self.client = self._init_s3_client()

    def upload_file(self, file: bytes, bucket_name: str, output_path: str) -> None:
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(file)
            tmp_path = tmp.name
        response = self.client.upload_file(tmp_path, bucket_name, output_path)
        print(response)
        os.remove(tmp_path)

    def _init_s3_client(self) -> boto3.client:
        return boto3.client(
            service_name='s3',
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY
        )
