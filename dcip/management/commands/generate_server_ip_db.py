import json
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
            self.download_json_ips(db)

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

    def download_json_ips(self, db):
        for entry in db.get("json_urls", []):
            try:
                req = urllib.request.Request(
                    entry["url"],
                    headers={"User-Agent": "django-dcip/1.0"},
                )
                with urllib.request.urlopen(req, timeout=30) as response:
                    data = json.loads(response.read().decode("utf-8"))
                    items = data.get(entry["key"], [])
                    for item in items:
                        if entry["field"]:
                            # Nested: {"prefixes": [{"ipv4Prefix": "8.8.8.0/24"}, ...]}
                            cidr = item.get(entry["field"])
                        else:
                            # Flat list: {"addresses": ["1.2.3.0/24", ...]}
                            cidr = item
                        if cidr and ":" not in str(cidr):
                            self.save_cidr(str(cidr), db["slug"])
            except Exception as e:
                self.stderr.write(
                    "Error downloading JSON %s: %s" % (entry["url"], e)
                )

    def save_cidr(self, cidr, provider):
        try:
            CidrAddress.objects.create(cidr=cidr, provider=provider)
        except IntegrityError:
            pass
