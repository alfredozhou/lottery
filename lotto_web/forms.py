from django.forms import ModelForm
from .models import LotteryTicket
from django import forms

class TicketForm(ModelForm):
	message = forms.CharField(widget=forms.Textarea)
	class Meta:
		model = LotteryTicket
