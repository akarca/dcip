from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from django.conf import settings


class Command(BaseCommand):
    help = "Upload db to minio"

    def handle(self, *args, **options):
        file_name = settings.DATABASES["server_ip"]["NAME"]
        with open(file_name, "rb") as file:
            file_name = default_storage.save(file_name, file)

        msg_args = (
            settings.AWS_S3_ENDPOINT_URL,
            settings.AWS_STORAGE_BUCKET_NAME,
            file_name,
        )
        print("DB uploaded to %s/%s/%s" % msg_args)
