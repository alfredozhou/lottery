from django.test import TestCase, RequestFactory, Client
from django.core.urlresolvers import resolve
from .views import index
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
		request_factory = RequestFactory()
		request = request_factory.post('/')
		request.session = {'name':'Juan Florencio', 'email':'jflorencio@gmail.com', 'password':'abcde', 'ver_password':'abcde', 'telephone':'2342342345'}
		
		register(request)

		u = User.objects.get(username='jflorencio@gmail.com')
		self.assertTrue(len(u) > 0)

		p = Player.objects.get(telephone='2342342345')
		self.assertTrue(len(p) > 0)

