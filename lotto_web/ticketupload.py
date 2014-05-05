from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
from models import Game, LotteryTicket, Player
from forms import UploadFileForm, EditUploadFileForm
from django.views.generic import FormView, DetailView, ListView
import pdb
from datetime import datetime


def show(request):
	lotto_games = Game.objects.all()
	return render_to_response('upload.html',  {'games': lotto_games}, context_instance=RequestContext(request))

def upload(request):
	userid = request.session['_auth_user_id']
	form = UploadFileForm(request.POST)
	form.is_valid()
	game = Game.objects.get(brand=form.cleaned_data['game'])
	date_to_draw = form.cleaned_data['lottery_date']
	player = Player.objects.get(user=userid)
	image = request.FILES['image']
	ticket = LotteryTicket(
			player = player,
			lottery_image = image,
			game = game,
			lottery_date = date_to_draw)
	ticket.save()
	return render_to_response('editTicket.html', {'image': ticket.lottery_image, 'ticketId': ticket.id}, context_instance=RequestContext(request))

def finishUploading(request):
	form = EditUploadFileForm(request.POST)
	form.is_valid()
	pdb.set_trace()
	print form.cleaned_data['numbers']
	return