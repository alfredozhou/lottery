from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
from models import Game
import pdb

def show(request):
	lotto_games = Game.objects.all()
	pdb.set_trace()
	return render_to_response('upload.html',  {'games': lotto_games}, context_instance=RequestContext(request))

def handle_uploaded_file(f):
	with open('some/file/name.txt', 'wb+') as destination:
		for chunk in f.chunks():
			destination.write(chunk)

def upload(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			handle_uploaded_file(request.FILES['file'])
    		return HttpResponseRedirect('/success/url/')
    else:
    	form = UploadFileForm()
    return show(request)
	