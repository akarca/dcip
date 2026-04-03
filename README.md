# django-dcip

Django app for detecting datacenter, cloud provider, and VPN IP addresses.

**Live demo & free API:** [https://ipaddress.world/datacenter-ip-checker/](https://ipaddress.world/datacenter-ip-checker/)

## Installation

```bash
pip install git+https://github.com/akarca/dcip.git
```

## Setup

1. Add to `INSTALLED_APPS`:

```python
INSTALLED_APPS = [
    ...
    "dcip",
]
```

2. Add the database router and SQLite database:

```python
DATABASES = {
    ...
    "server_ip": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "server_ip_db.sqlite3",
    },
}

DATABASE_ROUTERS = [..., "dcip.db_router.DCIPRouter"]
```

3. Include URLs (or wire them manually in your urlpatterns):

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("", include("dcip.urls")),
]
```

4. Populate the database:

```bash
python manage.py migrate --database=server_ip
python manage.py generate_server_ip_db
python manage.py merge_server_ip
```

## Free API

No API key required. Check any IPv4 address:

```
GET https://ipaddress.world/api/dcip/8.8.8.8/
```

```json
{
    "ip": "8.8.8.8",
    "is_datacenter": true,
    "provider": "gc",
    "provider_name": "Google"
}
```

### Examples

```bash
# curl
curl https://ipaddress.world/api/dcip/8.8.8.8/
```

```python
# Python
import requests
r = requests.get("https://ipaddress.world/api/dcip/8.8.8.8/")
print(r.json()["is_datacenter"])  # True
```

```javascript
// JavaScript
const r = await fetch("https://ipaddress.world/api/dcip/8.8.8.8/")
const data = await r.json()
console.log(data.is_datacenter) // true
```

## Tool Page

Visit `/datacenter-ip-checker/` for the web UI with IP input form and results.

## Providers

AWS, Google Cloud, Azure, DigitalOcean, Hetzner, Oracle, Linode, Akamai, Vultr, Cloudflare, Alibaba, and 50,000+ other datacenter ranges.

Database updated daily from public sources.

## Programmatic Usage

```python
from dcip.views import check_ip

is_datacenter, provider_slug, provider_name = check_ip("8.8.8.8")
# (True, "gc", "Google")
```

## License

MIT
