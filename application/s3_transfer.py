import uuid

import boto3
import requests

from application.config import Config


def upload_file_to_s3(cv_url=None):
    if cv_url is None:
        return None
    rq = requests.get(cv_url, stream=True)
    session = boto3.Session()
    s3 = session.resource('s3')
    bucket_name = Config.BUCKET_NAME

    s3_file_key = str(uuid.uuid1()) + '.pdf'
    bucket = s3.Bucket(bucket_name)
    bucket.upload_fileobj(rq.raw, s3_file_key)
    return f'https://{bucket_name}.s3.amazonaws.com/{s3_file_key}'


def remove_file_from_s3(s3_cv_url):
    if s3_cv_url is None:
        return None
    s3 = boto3.resource('s3')
    s3_file_key = s3_cv_url.split("amazonaws.com/", 1)[1]
    s3_obj = s3.Object(Config.BUCKET_NAME, s3_file_key)
    s3_obj.delete()
