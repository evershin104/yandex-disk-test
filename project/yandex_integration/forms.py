from django import forms
from django.core.exceptions import ValidationError


def validate_yandex_url(value: str) -> str:
    """
    Args:
        value:

    Returns:

    """
    if not value.startswith("https://disk.yandex.com/"):
        raise ValidationError("URL должен начинаться с 'https://disk.yandex.com/'")

    # Some kind of validation of given url
    # if not requests.get(url=YANDEX_CLOUD, params={'public_key': value}).ok:
    #     raise ValidationError("Публичный ключ недоступен")
    return value

class URLForm(forms.Form):
    url = forms.URLField(validators=[validate_yandex_url])
