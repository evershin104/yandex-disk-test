from django import forms
from django.core.exceptions import ValidationError

def validate_yandex_url(value):
    if not value.startswith("https://disk.yandex.com/d/"):
        raise ValidationError("URL должен начинаться с 'https://disk.yandex.com/d/'")
    return value

class URLForm(forms.Form):
    url = forms.URLField(validators=[validate_yandex_url])
