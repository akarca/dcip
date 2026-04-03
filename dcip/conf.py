from django.conf import settings

DEFAULT_SERVER_IP_URLS = [
    {"slug": "do", "name": "DigitalOcean", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/digitalocean/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/DIGITALOCEAN/only_ip_blocks.txt",
    ]},
    {"slug": "aw", "name": "Amazon AWS", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/amazon/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/AWS_EC2/only_ip_blocks.txt",
    ]},
    {"slug": "gc", "name": "Google", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/google/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/GOOGLE_CLOUD/only_ip_blocks.txt",
    ]},
    {"slug": "li", "name": "Linode", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/linode/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/LINODE/only_ip_blocks.txt",
    ]},
    {"slug": "az", "name": "Microsoft Azure", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/microsoft/ipv4_merged.txt",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/MICROSOFT/only_ip_blocks.txt",
    ]},
    {"slug": "oc", "name": "Oracle", "urls": [
        "https://raw.githubusercontent.com/lord-alfred/ipranges/main/oracle/ipv4_merged.txt",
    ]},
    {"slug": "ak", "name": "Akamai", "urls": [
        "https://raw.githubusercontent.com/SecOps-Institute/Akamai-ASN-and-IPs-List/master/akamai_ip_cidr_blocks.lst",
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/AKAMAI/only_ip_blocks.txt",
    ]},
    {"slug": "he", "name": "Hetzner", "urls": [
        "https://raw.githubusercontent.com/Pymmdrza/Datacenter_List_DataBase_IP/mainx/Hetzner/CIDR.txt",
    ]},
    {"slug": "ac", "name": "Alibaba", "urls": [
        "https://raw.githubusercontent.com/SM443/IP-Prefix-List/main/ALIBABA/only_ip_blocks.txt",
    ]},
    {"slug": "vu", "name": "Vultr", "urls": [
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/vultr/vultr_ips_merged_v4.txt",
    ]},
    {"slug": "cf", "name": "Cloudflare", "urls": [
        "https://raw.githubusercontent.com/rezmoss/cloud-provider-ip-addresses/main/cloudflare/cloudflare_ips_merged_v4.txt",
    ]},
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
