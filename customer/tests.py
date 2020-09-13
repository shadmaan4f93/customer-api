import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer

class CustomerTests(APITestCase):

    """ This test class will test customer api's  """

    url = reverse("customer-list")
    
    # defining static data to test create customer api.
    data = {
        "name": "test",
        "email": "test@example.com",
        "phone": "999999999999",
        "address": "Test address"
    }
    # Notes: This should be from a separate test file but for demo purpose, i have set as static.

    def test_create_customer(self):
        """ Ensure we can create a new customer object. """

        # Creating customer by calling customer create api
        response = self.client.post(self.url, self.data, format='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response_data["name"], 'test')
    
    def test_get_customer(self):
        """ Ensure we can get customer object. """

        # Creating customer by calling customer create api
        self.client.post(self.url, self.data, format='json')
        response = self.client.get(self.url)
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data[0]["name"], 'test')
    
    def test_update_customer(self):
        """ Ensure we can get customer object. """

        # Creating customer by calling customer create api
        response = self.client.post(self.url, self.data, format='json')
        response_data = json.loads(response.content)
        self.data["name"] = "test1"
        response = self.client.put(f'{self.url}{response_data["id"]}/', self.data, format='json')
        response_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data["name"], 'test1')
        self.assertEqual(response_data["email"], 'test@example.com')

    def test_delete_customer(self):
        """ Ensure we can delete customer object. """

        # Creating customer by calling customer create api
        response = self.client.post(self.url, self.data, format='json')
        response_data = json.loads(response.content)
        response = self.client.delete(f'{self.url}{response_data["id"]}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)