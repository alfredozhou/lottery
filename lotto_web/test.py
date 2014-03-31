from django.test import TestCase, RequestFactory
from django.core.urlresolvers import resolve
from .views import index


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