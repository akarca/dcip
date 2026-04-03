import ipaddress

from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.views.decorators.http import require_GET

from .conf import get_provider_names
from .models import MergedCidrAddress


def _get_client_ip(request):
    x_forwarded = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded:
        return x_forwarded.split(",")[0].strip()
    return request.META.get("REMOTE_ADDR")


def check_ip(ip_str):
    """Check if an IP is from a datacenter. Returns (is_datacenter, provider_slug, provider_name)."""
    try:
        ipaddress.ip_address(ip_str)
    except ValueError:
        return None, None, None

    provider_names = get_provider_names()
    match = MergedCidrAddress.objects.filter(cidr__contains=ip_str).first()
    if match:
        return True, match.provider, provider_names.get(match.provider, match.provider)
    return False, None, None


@require_GET
@cache_page(300)
def check_api(request, ip):
    """API endpoint: GET /api/dcip/<ip>/"""
    is_dc, slug, name = check_ip(ip)

    if is_dc is None:
        return JsonResponse({"error": "Invalid IP address"}, status=400)

    return JsonResponse({
        "ip": ip,
        "is_datacenter": is_dc,
        "provider": slug,
        "provider_name": name,
    })


@require_GET
def check_page(request):
    """Tool page: datacenter IP checker with form."""
    client_ip = _get_client_ip(request)
    result = None

    ip = request.GET.get("ip", "").strip()
    if ip:
        is_dc, slug, name = check_ip(ip)
        if is_dc is not None:
            result = {
                "ip": ip,
                "is_datacenter": is_dc,
                "provider": slug,
                "provider_name": name,
            }
        else:
            result = {"ip": ip, "error": True}

    return render(request, "dcip/check.html", {
        "client_ip": client_ip,
        "result": result,
        "query_ip": ip,
    })
