from django.test import TestCase
from website.models import Page


class WebsiteTests(TestCase):
    def setUp(self):
        self.page = Page.objects.create(name="Test Page", slug="test-page")

    def test_page_is_created(self):
        self.assertTrue(self.page)

    def test_page_slug_matches_expectation(self):
        self.assertTrue(self.page.slug == 'test-page')
