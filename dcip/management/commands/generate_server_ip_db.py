import urllib.request

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from dcip.conf import get_server_ip_urls
from dcip.models import CidrAddress


class Command(BaseCommand):
    help = "Download datacenter IP ranges and populate database"

    def handle(self, *args, **options):
        for db in get_server_ip_urls():
            self.stdout.write("Downloading %s..." % db["name"])
            self.download_server_ips(db)

    def download_server_ips(self, db):
        for url in db["urls"]:
            try:
                with urllib.request.urlopen(url, timeout=30) as response:
                    txt = response.read()
                    lines = txt.decode("utf-8").split("\n")
                    for line in lines:
                        line = line.strip()
                        if not line or ":" in line or "#" in line:
                            continue
                        self.save_cidr(line, db["slug"])
            except Exception as e:
                self.stderr.write("Error downloading %s: %s" % (url, e))

    def save_cidr(self, cidr, provider):
        try:
            CidrAddress.objects.create(cidr=cidr, provider=provider)
        except IntegrityError:
            pass
