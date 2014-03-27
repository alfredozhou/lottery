from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from datetime import datetime
from .models import User
from .forms import UserForm
from .forms import SigninForm
from .views import yearView
from django.db import IntegrityError
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
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
			user = User(
				name = form.cleaned_data['name'],
				telephone = form.cleaned_data['telephone'],
				username= form.cleaned_data['email'],
				email = form.cleaned_data['email'],
				password = form.cleaned_data['password'])
			try:
				user.save()
			except IntegrityError:
				form.addError(user.email + ' is already a member')
		else:
			request.session['user'] = user.pk
			return HttpResponseRedirect('/')
	else:
		form = UserForm()
	request.session['user'] = user
	return yearView(request)

def sign_in(request):
	form = SigninForm(request.POST)
	if form.is_valid():
		username = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)
		pdb.set_trace()
		if user is not None:
			login(request, user)
			return HttpResponseRedirect('/')
		else:
			form.addError('Incorrect email address or password')
	return render_to_response('sign_in.html', {'form': form},context_instance=RequestContext(request))


def sign_out(request):
	logout(request)
	return HttpResponseRedirect('/')