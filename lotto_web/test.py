from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve
from .views import index
from .models import Player
from .registration import register
from django.contrib.auth.models import User


class LotteryTests(TestCase):
	def testUsingCorrectHtml(self):
		index = self.client.get('/')
		self.assertTemplateUsed(index, 'index.html')

	def test_uses_index_html_template2(self):
		request_factory = RequestFactory()
		request = request_factory.get('/')
		request.session = {}

		resp = index(request)
		
		self.assertContains(resp, "<title>Lottery Genius</title>")

	def test_registering_for_new_user(self):
		input_map = {'name':'Juan Florencio', 'email':'jflorencio@gmail.com', 'password':'abcde', 'ver_password':'abcde', 'telephone':'2342342345'}
		response = self.client.post('/register', input_map)
	
		u = User.objects.get(username='jflorencio@gmail.com')
		self.assertTrue(u is not None)

		p = Player.objects.get(telephone='2342342345')
		self.assertTrue(p is not None)

	def test_sign_in_for_user(self):
		user = User.objects.create_user(
				first_name='Fred',
				last_name='Mundy',
				username= 'f@mundy.com',
				email = 'f@mundy.com',
				password = 'password')
		input_map = {'email':'f@mundy.com', 'password':'password'}
		response = self.client.post('/sign-in', input_map)
		self.assertRedirects(response, '/')

