from django_any import any_model
from django.core.urlresolvers import reverse, NoReverseMatch
from django.test import Client, TestCase

from products.models import Product

class CategoryTest(TestCase):
    """Test of the category part of the listing page."""
    def test_no_category(self):
        """Can we request a non-existing category?"""
        with self.assertRaises(NoReverseMatch):
            self.client.get(reverse('category'), kwaegs={"category": "bad"})

    def test_good_category(self):
        """Can we request all the existing category?"""
        for category in ['kids', 'kid_adult', 'women']:
            response = self.client.get(reverse('category',
                                       kwargs={'category': category}))
            self.assertTrue(response.status_code == 200)

    def test_only_returns_category_items(self):
        """Test that only the products matching the category is returned."""
        any_model(Product, kids=0, kid_adult=0, women=0)
        kid_product = any_model(Product, kids=1, kid_adult=0, women=0)
        response = self.client.get(reverse('category',
                                       kwargs={'category': 'kids'}))
        self.assertTrue(len(response.context['listing']) == 1)
        self.assertTrue(response.context['listing'][0] == kid_product)


class DetailsTest(TestCase):
    """Test of the details page."""
    def test_200_on_existing_product(self):
        """Sanity check that a 200 is returned for good requests."""
        any_model(Product, kids=0, kid_adult=0, women=0, id=1)
        response = self.client.get(reverse('details', kwargs={'pk': 1}))
        self.assertTrue(response.status_code == 200)

    def test_404_on_missing_product(self):
        response = self.client.get(reverse('details', kwargs={'pk': 1}))
        self.assertTrue(response.status_code == 404)

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
