from django.forms import ModelForm
from .models import LotteryTicket
from django import forms

class ImageUploadForm(forms.Form):
    """Image upload form."""
    image = forms.ImageField()
