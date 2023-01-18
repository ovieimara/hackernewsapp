from django.test import TestCase

# Create your tests here.
class NewsAppTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_news(self):
        url = "/app/news"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200, 'review response')
