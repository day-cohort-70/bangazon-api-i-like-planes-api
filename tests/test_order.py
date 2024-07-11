import json
from rest_framework import status
from rest_framework.test import APITestCase
from bangazonapi.models import Order,Customer,Payment


class OrderTests(APITestCase):

    def setUp(self):
        """
        Create a new account and create sample category
        """
        url = "/register"
        data = {"username": "steve", "password": "Admin8*", "email": "steve@stevebrownlee.com",
                "address": "100 Infinity Way", "phone_number": "555-1212", "first_name": "Steve", "last_name": "Brownlee"}
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Create a payment type
        url = "/paymenttypes"
        data = {"merchant_name": "Visa", "account_number": "24ijio68948fj8439", "expiration_date": "2020-01-01"}
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.payment_id = response.data['id']
        
    def test_add_payment_type_to_order(self):
        """
        Ensure we can add a payment type to an order with the PUT method.
        """
        # creating an object instance based on the order model that has the same properties line 34
        order = Order()
        order.customer = Customer.objects.get(id=1)
        order.created_date = "2024-07-11"
        order.save()

        # create test body and DEFINE PROPERTIES FOR ORDER
        data = {
            "payment_type": self.payment_id
        }

        print(data)

        response = self.client.put(f"/orders/{order.id}", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET order again to verify changes were made
        response = self.client.get(f"/orders/{order.id}")
        json_response = json.loads(response.content)

        # Assert that the properties are correct
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(json_response)
        self.assertEqual(json_response["payment_type"]["id"], 1)