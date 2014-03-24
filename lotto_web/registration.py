from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
import megamillions_lottery_value as megamillions
import powerball_value as poweball


def start_registering(request):
	return render_to_response('register.html', context_instance=RequestContext(request))

def register(request):
	return render_to_response('index.html', context_instance=RequestContext(request))

def sign_in(request):
	return render_to_response('lotto-years.html', context_instance=RequestContext(request))

def sign_out(request):
	return render_to_response('calendar-svg.html', context_instance=RequestContext(request))