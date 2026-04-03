from netaddr import IPSet

from django.core.management.base import BaseCommand
from django.db.utils import IntegrityError

from dcip.conf import get_server_ip_urls
from dcip.models import CidrAddress, MergedCidrAddress


class Command(BaseCommand):
    help = "Merge overlapping CIDR blocks into optimized table"

    def handle(self, *args, **options):
        for item in get_server_ip_urls():
            slug = item["slug"]
            cidrs = [
                str(cidr)
                for cidr in CidrAddress.objects.filter(provider=slug).values_list(
                    "cidr", flat=True
                )
            ]
            nets = IPSet(cidrs)
            for net in nets.iter_ipranges():
                for cidr in net.cidrs():
                    try:
                        MergedCidrAddress.objects.create(cidr=str(cidr), provider=slug)
                    except IntegrityError:
                        pass
            self.stdout.write("%s: %d merged CIDRs" % (item["name"], MergedCidrAddress.objects.filter(provider=slug).count()))
