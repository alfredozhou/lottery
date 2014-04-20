from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.template import Context, loader
from datetime import datetime
from models import Game, LotteryTicket, Player
from forms import UploadFileForm
from django.views.generic import FormView, DetailView, ListView


def show(request):
	lotto_games = Game.objects.all()
	return render_to_response('upload.html',  {'games': lotto_games}, context_instance=RequestContext(request))

class LotteryImageUpload(FormView):
	template_name = 'editTicket.html'
	form_class = UploadFileForm

	def form_valid(self, form):
		userid = request.session['user']
		ticket = LotteryTicket(
			player = PLayer.objects.filter(user=userid),
			lottery_image =  self.get_form_kwargs().get('files')['image'],
			game= self.get_form_kwargs().get('game-ticket'),
			lottery_date = self.get_form_kwargs().get('lottery_date'))
		ticket.save()
		self.id=ticket.id
		return render_to_response('editTicket.html', {'form': form}, context_instance=RequestContext(request))



upload = LotteryImageUpload.as_view()

class LotteryImageEdit(FormView):
	form_class = UploadFileForm

	def form_valid(self, form):
		ticket = UploadFileForm(image = self.get_form_kwargs().get('files')['image'],
			game= self.get_form_kwargs().get('game-ticket'),
			lottery_date = self.get_form_kwargs().get('lottery_date'))

finishUploading = LotteryImageEdit.as_view()