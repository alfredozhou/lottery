from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
from models import Game

def show(request):
	t = loader.get_template('upload.html')
	lotto_games = Game.objects.all()
	c = Context({
		'games': lotto_games
		})
	return HttpResponse(t.render(c))

def upload(request):
	return render_to_response('lotto-years.html', context_instance=RequestContext(request))