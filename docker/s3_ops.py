import boto3
from botocore.exceptions import ClientError

class S3Ops:
    def __init__(self):
        self.s3Client = boto3.client('s3')
        self.s3Resource = boto3.resource('s3')
        self.bucketName='tom-testing'

    def stream(self, data, fileName):
        """
        Summary: Streams data from memory to s3 with fileName passed.
        Params: data (Bytes Object) - Data stored in memory to be streamed to s3
                fileName (STRING) - The name of the file data is to be
                    written to in s3
        Return: s3Path (STRING) - The path to streamed file in s3
        """
        try:
            # streams data to s3
            upload = self.s3Resource.Object(self.bucketName, key).put(Body=data)
            # Create path to stream data to on s3
            s3Path = 's3://{0}/{1}'.format(self.bucketName, fileName)
            return s3Path
        except (ClientError, Exception) as e:
            # reports failure to dynamodb
            raise ValueError('s3=fail')
