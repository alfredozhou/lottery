from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
import megamillions_lottery_value as megamillions
import powerball_value as poweball


def index(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def yearView(request):
	return render_to_response('lotto-years.html', context_instance=RequestContext(request))

def better_lotto_status(request):
	t = loader.get_template('lotto-display.html')
	million = 1000000
	mega_prize = int(megamillions.get_prize()) * million
	power_prize = int(poweball.get_prize()) * million
	mega_threshold = megamillions.threshold()
	power_threshold = poweball.threshold()
	c = Context({
		'mega_worthit': mega_prize > mega_threshold, 
		'mega_prize': mega_prize,
		'mega_threshold': mega_threshold,
		'power_worthit': power_prize > power_threshold,
		'power_prize': power_prize,
		'power_threshold': power_threshold
		})
	return HttpResponse(t.render(c))
