from storages.backends.s3boto import S3BotoStorage


def StaticS3BotoStorage():
    return S3BotoStorage(location="benchmark/static")

def MediaS3BotoStorage():
    return S3BotoStorage(location="benchmark/media")
