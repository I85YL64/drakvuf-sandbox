#!/usr/bin/env python

from karton2 import Config
from karton2.services.system import SystemService
from drakcore.util import find_config


def main():
    config = Config(find_config())
    service = SystemService(config)

    bucket_name = config.minio_config["bucket"]
    minio = service.minio
    service.log.info("Veryfing bucket existence...")
    if not minio.bucket_exists(bucket_name):
        service.log.info("Bucket %s is missing. Creating new one...", bucket_name)
        minio.make_bucket(bucket_name)

    service.loop()


if __name__ == "__main__":
    main()
