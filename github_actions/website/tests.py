from django.test import TestCase
from website.models import Page


class WebsiteTests(TestCase):
    def test_page_is_created(self):
        page = Page.objects.create(name="Test Page", slug="test-page")
        self.assertTrue(page)
