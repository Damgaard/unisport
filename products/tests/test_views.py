from django_any import any_model
from django.core.urlresolvers import reverse
from django.test import Client, TestCase

from products.models import Product

class HomeTest(TestCase):
    """Test suite for the homepage where a product listing is shown."""
    def test_200(self):
        """Sanity check. Does the page work."""
        response = self.client.get(reverse('home'))
        self.assertTrue(response.status_code == 200)

    def test_empty_listing(self):
        """Test that the listing is empty if there are no products in DB."""
        response = self.client.get(reverse('home'))
        self.assertTrue(len(response.context['listing']) == 0)

    def test_includes_product(self):
        """If there is a product, test that it will be in the listing."""
        product = any_model(Product, kids=0, kid_adult=0, women=0)
        response = self.client.get(reverse('home'))
        self.assertTrue(len(response.context['listing']) == 1)
        self.assertTrue(product in response.context['listing'])

    def test_listing_ordering(self):
        """Test that listing is sorted cheapest first."""
        product1 = any_model(Product, kids=0, kid_adult=0, women=0, price="10")
        product2 = any_model(Product, kids=0, kid_adult=0, women=0, price="5")
        product3 = any_model(Product, kids=0, kid_adult=0, women=0, price="5.75")
        response = self.client.get(reverse('home'))
        self.assertTrue(len(response.context['listing']) == 3)
        self.assertTrue(response.context['listing'][0] == product2)

    def test_listing_max_ten_items(self):
        """Ensure only up to ten items are returned, no matter how many elements in DB."""
        for _ in range(25):
            any_model(Product, kids=0, kid_adult=0, women=0, price="10")
        self.assertTrue(Product.objects.all().count() == 25)
        response = self.client.get(reverse('home'))
        self.assertTrue(len(response.context['listing']) == 10)
