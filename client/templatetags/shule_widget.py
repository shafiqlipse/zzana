from django import template
from django.utils.http import urlencode
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def shule_widget(school="stahiza"):
    """
    Generates a clickable referral link for Shule widget.
    """
    base_url = "https://shule.tv/login"
    params = {"referral": school}
    referral_url = f"{base_url}?{urlencode(params)}"
    return format_html('<a href="{}" target="_blank">Access Lessons Now</a>', referral_url)
