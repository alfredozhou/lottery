from django.http import HttpResponse
from django.template import Context, loader
from datetime import datetime


def show_lotto_status(request):
	return HttpResponse('<html><body>Time to buy lotto!</body></html>')

def better_lotto_status(request):
	t = loader.get_template('lotto-display.html')
	c = Context({'powerball_worth': True, 'megamillions_worth': False})
	return HttpResponse(t.render(c))
