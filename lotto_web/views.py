from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
import megamillions_lottery_value as megamillions
import powerball_value as poweball
from models import User
import pdb

def index(request):
	t = loader.get_template('index.html')
	c = RequestContext(request, {'at_home': True})
	return HttpResponse(t.render(c))
	
def yearView(request):
	t = loader.get_template('lotto-years.html')
	c = RequestContext(request, {'fat': True})
	return HttpResponse(t.render(c))

def svgView(request):
	return render_to_response('calendar-svg.html', context_instance=RequestContext(request))

def better_lotto_status(request):
	t = loader.get_template('lotto-display.html')
	million = 1000000
	mega_prize = int(megamillions.get_prize()) * million
	power_prize = int(poweball.get_prize()) * million
	mega_threshold = megamillions.threshold()
	power_threshold = poweball.threshold()
	c = RequestContext(request, {
		'mega_worthit': mega_prize > mega_threshold, 
		'mega_prize': mega_prize,
		'mega_threshold': mega_threshold,
		'power_worthit': power_prize > power_threshold,
		'power_prize': power_prize,
		'power_threshold': power_threshold
		})
	return HttpResponse(t.render(c))
