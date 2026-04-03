import os

from django.conf import settings
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Download db from minio"

    def handle(self, *args, **options):
        file_name = settings.DATABASES["server_ip"]["NAME"]

        remote_file = default_storage.open(file_name)

        os.makedirs(os.path.dirname(os.path.abspath(file_name)), exist_ok=True)

        with open(file_name, "wb") as local_file:
            local_file.write(remote_file.read())

        msg_args = (
            settings.AWS_S3_ENDPOINT_URL,
            settings.AWS_STORAGE_BUCKET_NAME,
            file_name,
        )
        print("DB downloaded from %s/%s/%s" % msg_args)
