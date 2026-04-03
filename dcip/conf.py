from django.conf import settings

DEFAULT_SERVER_IP_URLS = [
    # --- Major cloud providers ---
    {"slug": "gc", "name": "Google", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/google/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/GOOGLE_CLOUD/only_ip_blocks.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/googlecloud/googlecloud_ips_v4.txt",
    ], "json_urls": [
        {"url": "https://www.gstatic.com/ipranges/goog.json", "key": "prefixes", "field": "ipv4Prefix"},
        {"url": "https://www.gstatic.com/ipranges/cloud.json", "key": "prefixes", "field": "ipv4Prefix"},
    ]},
    {"slug": "aw", "name": "Amazon AWS", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/amazon/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/AWS_EC2/only_ip_blocks.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/aws/aws_ips_v4.txt",
    ], "json_urls": [
        {"url": "https://ip-ranges.amazonaws.com/ip-ranges.json", "key": "prefixes", "field": "ip_prefix"},
    ]},
    {"slug": "az", "name": "Microsoft Azure", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/microsoft/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/MICROSOFT/only_ip_blocks.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/azure/azure_ips_v4.txt",
    ]},
    {"slug": "do", "name": "DigitalOcean", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/digitalocean/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/DIGITALOCEAN/only_ip_blocks.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/digitalocean/digitalocean_ips_v4.txt",
    ]},
    {"slug": "oc", "name": "Oracle", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/oracle/ipv4_merged.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/oracle/oracle_ips_v4.txt",
    ]},
    {"slug": "li", "name": "Linode", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/linode/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/LINODE/only_ip_blocks.txt",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/linode/linode_ips_v4.txt",
    ]},
    # --- CDN / Edge providers ---
    {"slug": "cf", "name": "Cloudflare", "urls": [
        "https://www.cloudflare.com/ips-v4",
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/cloudflare/cloudflare_ips_v4.txt",
    ]},
    {"slug": "ak", "name": "Akamai", "urls": [
        "https://raw.githubusercontent.com/SecOps-Institute/Akamai-ASN-and-IPs-List/master/akamai_ip_cidr_blocks.lst",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/AKAMAI/only_ip_blocks.txt",
    ]},
    {"slug": "fa", "name": "Fastly", "urls": [
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/fastly/fastly_ips_v4.txt",
    ], "json_urls": [
        {"url": "https://api.fastly.com/public-ip-list", "key": "addresses", "field": None},
    ]},
    # --- Hosting providers ---
    {"slug": "he", "name": "Hetzner", "urls": [
        "https://raw.githubusercontent.com/Pymmdrza/Datacenter_List_DataBase_IP/mainx/Hetzner/CIDR.txt",
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/hetzner/hetzner_plain_ipv4.txt",
    ]},
    {"slug": "ov", "name": "OVH", "urls": [
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/ovh/ovh_plain_ipv4.txt",
    ]},
    {"slug": "sc", "name": "Scaleway", "urls": [
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/scaleway/scaleway_plain_ipv4.txt",
    ]},
    {"slug": "vu", "name": "Vultr", "urls": [
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/vultr/vultr_ips_v4.txt",
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/constant/constant_plain_ipv4.txt",
    ]},
    {"slug": "co", "name": "Contabo", "urls": [
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/contabo/contabo_plain_ipv4.txt",
    ]},
    {"slug": "ac", "name": "Alibaba", "urls": [
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/ALIBABA/only_ip_blocks.txt",
    ]},
    {"slug": "gh", "name": "GitHub", "urls": [
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/github/github_ips_v4.txt",
    ]},
    {"slug": "gr", "name": "Gcore", "urls": [
        "https://raw.githubusercontent.com/123jjck/cdn-ip-ranges/main/gcore/gcore_plain_ipv4.txt",
    ]},
    # --- Broad datacenter lists ---
    {"slug": "ot", "name": "Others", "urls": [
        "https://raw.githubusercontent.com/jhassine/server-ip-addresses/master/data/datacenters.txt",
    ]},
]


def get_server_ip_urls():
    return getattr(settings, "SERVER_IP_URLS", DEFAULT_SERVER_IP_URLS)


def get_provider_choices():
    return [(item["slug"], item["name"]) for item in get_server_ip_urls()]


def get_provider_names():
    return {item["slug"]: item["name"] for item in get_server_ip_urls()}
