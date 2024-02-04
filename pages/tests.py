from django.test import SimpleTestCase
from django.urls import resolve, reverse

from pages.views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_home_page_contains_correct_html(self):
        response = self.client.get("/")
        self.assertContains(response, "Home")

    def test_home_page_does_not_contain_incorrect_html(self):
        response = self.client.get("/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_home_page_url_resolves_home_page_view(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)


class AboutPageTests(SimpleTestCase):
    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_about_page_contains_correct_html(self):
        response = self.client.get("/about/")
        self.assertContains(response, "About")

    def test_about_page_does_not_contain_incorrect_html(self):
        response = self.client.get("/about/")
        self.assertNotContains(response, "Hi there! I should not be on the page.")

    def test_about_page_url_resolves_about_page_view(self):
        view = resolve("/about/")
        self.assertEqual(view.func.__name__, AboutPageView.as_view().__name__)

    def test_url_available_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
