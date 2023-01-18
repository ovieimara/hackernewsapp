from django.test import TestCase

# Create your tests here.
class NewsAppTest(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def test_latest_news(self):
        url = "/api/latest"
        response = self.client.get(url)
        json = response.json()
        item, *_ = json
        self.assertGreater(len(json), 5, 'review response')
        self.assertEqual(type(item), dict or list, 'review response')
        self.assertEqual(type(item.get('item_id')), int, 'review response')
        self.assertEqual(response.status_code, 200, 'review response')

