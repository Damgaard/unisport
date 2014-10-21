from django.test import TestCase
from django_any import any_model

from products.models import Product

class ProductTest(TestCase):
    """Testsuite for the Product model."""
    def test_demographics_save_error(self):
        """Ensure error is thrown on multiple demographics selected."""
        with self.assertRaises(TypeError):
            any_model(Product, kids=1, kid_adult=1, women=0)

    def test_demographics_save_one_set(self):
        """Ensure no error is thrown if 1 demographic is set."""
        any_model(Product, kids=0, kid_adult=1, women=0)

    def test_demographics_save_nothing_set(self):
        """Ensure no error is thrown if no demographic is set."""
        any_model(Product, kids=0, kid_adult=0, women=0)
