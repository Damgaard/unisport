from django.core.urlresolvers import reverse
from django.test import Client, TestCase

class HomeTest(TestCase):
    def test_200(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertTrue(response.status_code == 200)
