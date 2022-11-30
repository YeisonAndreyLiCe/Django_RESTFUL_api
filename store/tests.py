#from django.test import TestCase
from rest_framework.test import APITestCase
from store.models import Product

import os.path
from django.conf import settings

class ProductCreateTestsCase(APITestCase):
    def test_create_product(self):
        data = {
            'name': 'iPhone 12',
            'price': 999.99,
            'description': 'A new iPhone',
        }
        response = self.client.post('/api/v1/products/create/', data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get().name, 'iPhone 12')
        for attr, expected_value in data.items():
            self.assertEqual(getattr(Product.objects.get(), attr), expected_value)
        self.assertEqual(response.data['is_on_sale'], False)
        self.assertEqual(response.data['current_price'], float(data['price']))

""" class ProductDestroyTestsCase(APITestCase):
    def test_delete_product(self):
        product = Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        response = self.client.delete(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0) """

class ProductListTestCase(APITestCase):
    def test_list_products(self):
        count = Product.objects.count()
        Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        Product.objects.create(
            name='iPhone 12 Pro',
            price=1099.99,
            description='A new iPhone',
        )
        response = self.client.get('/api/v1/products/')
        objects = Product.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Product.objects.count(), 2 + count)
        self.assertEqual(len(response.data['results']), 2 + count)
        self.assertEqual(response.data['results'][0]['name'], 'iPhone 12')
        self.assertEqual(response.data['results'][1]['name'], 'iPhone 12 Pro') 

class ProductRetrieveUpdateDestroyTestCase(APITestCase):
    def test_retrieve_product(self):
        product = Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        response = self.client.get(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'iPhone 12')
        self.assertEqual(float(response.data['price']), 999.99)
        self.assertEqual(response.data['description'], 'A new iPhone')

    def test_update_product(self):
        product = Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        data = {
            'name': 'iPhone 12 Pro',
            'price': 1099.99,
            'description': 'A new iPhone',
        }
        response = self.client.patch(f'/api/v1/products/{product.id}/', data=data)
        print(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['name'], 'iPhone 12 Pro')
        self.assertEqual(float(response.data['price']), 1099.99)
        self.assertEqual(response.data['description'], 'A new iPhone')

    def test_upload_product_photo(self):
        product = Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        with open(os.path.join(settings.BASE_DIR, 'store', 'tests', 'iphone12.jpg'), 'rb') as f:
            response = self.client.post(f'/api/v1/products/{product.id}/upload_photo/', data={'photo': f})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['photo'], f'http://testserver/media/{product.photo}')

    def test_delete_product(self):
        product = Product.objects.create(
            name='iPhone 12',
            price=999.99,
            description='A new iPhone',
        )
        response = self.client.delete(f'/api/v1/products/{product.id}/')
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Product.objects.count(), 0)