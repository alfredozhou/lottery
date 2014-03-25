from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from datetime import datetime
from .models import Person
from .forms import UserForm
from .views import yearView
from django.db import IntegrityError
from django.http import HttpResponseRedirect



def start_registering(request):
	return render_to_response('register.html', context_instance=RequestContext(request))

def register(request):
	user = None
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			user = Person(
				name = form.cleaned_data['name'],
				telephone = form.cleaned_data['telephone'],
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
	request.session['user'] = user.pk
	return yearView(request)

def sign_in(request):
	return render_to_response('lotto-years.html', context_instance=RequestContext(request))

def sign_out(request):
	del request.session['user']
	return HttpResponseRedirect('/')