from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
from models import Game

def show(request):
	lotto_games = Game.objects.all()
	return render_to_response('upload.html',  {'games': lotto_games}, context_instance=RequestContext(request))
	
def upload(request):
	return render_to_response('lotto-years.html', context_instance=RequestContext(request))