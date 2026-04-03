import json
import urllib.request

from django.core.management.base import BaseCommand

from dcip.conf import get_server_ip_urls
from dcip.models import CidrAddress


class Command(BaseCommand):
    help = "Download datacenter IP ranges and populate database"

    def handle(self, *args, **options):
        for db in get_server_ip_urls():
            self.stdout.write("Downloading %s..." % db["name"])
            cidrs = set()
            self._collect_text_urls(db, cidrs)
            self._collect_json_urls(db, cidrs)
            self._bulk_save(cidrs, db["slug"])
            self.stdout.write("  %s: %d CIDRs" % (db["name"], len(cidrs)))

    def _collect_text_urls(self, db, cidrs):
        for url in db["urls"]:
            try:
                req = urllib.request.Request(
                    url, headers={"User-Agent": "django-dcip/1.0"}
                )
                with urllib.request.urlopen(req, timeout=30) as response:
                    txt = response.read().decode("utf-8")
                    for line in txt.split("\n"):
                        line = line.strip()
                        if not line or ":" in line or "#" in line:
                            continue
                        cidrs.add(line)
            except Exception as e:
                self.stderr.write("  Error %s: %s" % (url, e))

    def _collect_json_urls(self, db, cidrs):
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
                            cidr = item.get(entry["field"])
                        else:
                            cidr = item
                        if cidr and ":" not in str(cidr):
                            cidrs.add(str(cidr))
            except Exception as e:
                self.stderr.write(
                    "  Error JSON %s: %s" % (entry["url"], e)
                )

    def _bulk_save(self, cidrs, provider):
        existing = set(
            CidrAddress.objects.filter(provider=provider).values_list(
                "cidr", flat=True
            )
        )
        new_cidrs = cidrs - existing
        if new_cidrs:
            batch = [
                CidrAddress(cidr=cidr, provider=provider) for cidr in new_cidrs
            ]
            CidrAddress.objects.bulk_create(batch, batch_size=500, ignore_conflicts=True)
