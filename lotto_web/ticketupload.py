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
from .views import yearView


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

def parseTicketNumbers(numbers_in_string, ticketId):
	ticket = LotteryTicket.objects.get(id=ticketId)
	numbers = []
	for line in numbers_in_string.split('\n'):
		linecontent = line.split(' ')
		number = LotteryNumber(ticket=ticket, 
			number1=Integer(linecontent[0]),
			number2=Integer(linecontent[1]),
			number3=Integer(linecontent[2]),
			number4=Integer(linecontent[3]),
			number5=Integer(linecontent[4]),
			ball=Integer(linecontent[5]))
		numbers.append(number)
	return numbers


def finishUploading(request):
	form = EditUploadFileForm(request.POST)
	form.is_valid()
	text_values = form.cleaned_data['numbers']
	pdb.set_trace()	
	ticketId = int(form.cleaned_data['ticketId'])
	ticketnumbers = parseTicketNumbers(text_values, ticketId)
	pdb.set_trace()
	for number in ticketnumbers:
		number.save()
	return yearView(request);
	