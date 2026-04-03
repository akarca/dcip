# django-dcip

Django app for detecting datacenter, cloud provider, and VPN IP addresses.

## Installation

```bash
pip install git+https://github.com/NameOcean/dcip.git
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

3. Include URLs:

```python
from django.urls import include, path

urlpatterns = [
    ...
    path("", include("dcip.urls")),
]
```

4. Run migrations and populate the database:

```bash
python manage.py migrate --database=server_ip
python manage.py generate_server_ip_db
python manage.py merge_server_ip
```

## API

```
GET /api/dcip/8.8.8.8/

{
    "ip": "8.8.8.8",
    "is_datacenter": true,
    "provider": "gc",
    "provider_name": "Google"
}
```

## Tool Page

Visit `/datacenter-ip-checker/` for the web UI.

## Providers

AWS, Google Cloud, Azure, DigitalOcean, Hetzner, Oracle, Linode, Akamai, Vultr, Cloudflare, Alibaba, and 50,000+ other datacenter ranges.

## Programmatic Usage

```python
from dcip.views import check_ip

is_datacenter, provider_slug, provider_name = check_ip("8.8.8.8")
```
