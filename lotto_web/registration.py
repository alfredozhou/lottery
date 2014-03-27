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
	user = None
	redirect_to = request.REQUEST.get('next', '')
	if request.method == 'POST':
		form = SigninForm(request.POST)
		if form.is_valid():
			results = User.objects.filter(email=form.cleaned_data['email'])
			if len(results) == 1:
				if results[0].check_password(form.cleaned_data['password']):
					request.session['user'] = results[0].pk
					return HttpResponseRedirect('/')
				else:
					form.addError('Incorrect email address or password')
			else:
				form.addError('Incorrect email address or password')
	else:
		form = SigninForm()
		print form.non_field_errors()
	return render_to_response('sign_in.html',{'form': form, 'user': user},context_instance=RequestContext(request))



def sign_out(request):
	del request.session['user']
	return HttpResponseRedirect('/')