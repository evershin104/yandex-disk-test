from django import forms
from django.core.exceptions import ValidationError


def validate_yandex_url(value: str) -> str:
    """Check if value starts with yandex hostname
    Args:
        value: given value into form
    Returns:
        value if its OK
    Raises:
        ValidationError if value does not start with yandex hostname
    """
    if not value.startswith("https://disk.yandex.com/"):
        raise ValidationError("URL должен начинаться с 'https://disk.yandex.com/'")

    # Some kind of validation of given url
    # if not requests.get(url=YANDEX_CLOUD, params={'public_key': value}).ok:
    #     raise ValidationError("Публичный ключ недоступен")
    return value

class URLForm(forms.Form):
    url = forms.URLField(validators=[validate_yandex_url])
