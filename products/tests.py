from django.test import TestCase
from .models import Product

# Create your tests here.
class ProductTest(TestCase):
    '''define the tests you eill run against prodcut model'''
    
    def test_str(self):
        test_name = Product(name='A Product')
        self.assertEqual(str(test_name), 'A Product')
