from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from datetime import datetime
from .models import Player
from .forms import UserForm
from .forms import SigninForm
from .views import yearView
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
import pdb



def start_registering(request):
	t = loader.get_template('register.html')
	c = RequestContext(request, {'at_sign_up': True})
	return HttpResponse(t.render(c))
	
def register(request):
	user = None
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			full_name = form.cleaned_data['name']
			names = full_name.split()
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			user = User.objects.create_user(
				first_name=names[0],
				last_name=names[1] if len(names) > 1 else "",
				username= email,
				email = email,
				password = password)
			player = Player.objects.create(user=user, 
				name=full_name, 
				telephone = form.cleaned_data['telephone'])
			try:
				user.save()
				player.save()
				user = authenticate(username=email, password=password)
				login(request, user)
				return render_to_response('index.html', {'user': user,'at_home': True}, context_instance=RequestContext(request))
			except IntegrityError:
				form.addError(user.email + ' is already a member')
	return render_to_response('register.html', {'form': form, 'at_sign_up': True},context_instance=RequestContext(request))
	
def sign_in(request):
	form = SigninForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return render_to_response('lotto-years.html', {'fat': True,'user': user },context_instance=RequestContext(request))
		else:
			form.addError('Incorrect email address or password')
	return render_to_response('sign_in.html', {'form': form},context_instance=RequestContext(request))


def sign_out(request):
	logout(request)
	return HttpResponseRedirect('/')