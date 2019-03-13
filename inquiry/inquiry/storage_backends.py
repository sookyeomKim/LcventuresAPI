from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    default_acl = 'public-read'


class UploadStorage(S3Boto3Storage):
    location = 'inquiry'
    file_overwrite = True
