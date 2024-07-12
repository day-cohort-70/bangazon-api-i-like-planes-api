import datetime
import json
from rest_framework import status
from rest_framework.test import APITestCase
from bangazonapi.models import Payment


class PaymentTests(APITestCase):
    def setUp(self) -> None:
    
        url = "/register"
        data = {"username": "steve", "password": "Admin8*", "email": "steve@stevebrownlee.com",
                "address": "100 Infinity Way", "phone_number": "555-1212", "first_name": "Steve", "last_name": "Brownlee"}
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)
        self.token = json_response["token"]
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_payment_type(self):
        """
        Ensure we can add a payment type for a customer.
        """
        # Add product to order
        url = "/paymenttypes"
        data = {
            "merchant_name": "American Express",
            "account_number": "111-1111-1111",
            "expiration_date": "2024-12-31",
            "create_date": datetime.date.today()
        }
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token)
        response = self.client.post(url, data, format='json')
        json_response = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(json_response["merchant_name"], "American Express")
        self.assertEqual(json_response["account_number"], "111-1111-1111")
        self.assertEqual(json_response["expiration_date"], "2024-12-31")
        self.assertEqual(json_response["create_date"], str(datetime.date.today()))

    def test_delete_payment_type(self):
        payment = Payment()
        payment.id = 1
        payment.merchant_name = "test name"
        payment.account_number = 1234
        payment.customer_id = 1
        payment.expiration_date = "2023-12-12"
        payment.create_date = "2024-01-01"
        payment.save()

        # DELETE the payment you just created
        response = self.client.delete(f"/paymenttypes/{payment.id}")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # GET the payment again to verify you get a 404 response
        response = self.client.get(f"/paymenttypes/{payment.id}")
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)