from django.test import TestCase
from django.core.urlresolvers import resolve
from lotto_web.views import index

class MainPageTests(TestCase):
	def test_root_resolves_to_main_view(self):
		main_page = resolve('/')
		self.assertEqual(main_page.func, index)

	def test_returns_appropriate_html(self):
		index = self.client.get('/')
		self.assertEquals(index.status_code, 200)