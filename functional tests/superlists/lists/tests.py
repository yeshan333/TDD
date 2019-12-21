from django.test import TestCase
from django.urls import resolve
from lists.views import home_page
# from django.core.urlresolvers import resolve # low version


""" # Create your tests here.
class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEqual(1+1, 3, 'bad calculate!')
"""

class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # 解析URL，将其映射到相应的视图函数上
        self.assertEqual(found.func, home_page)
