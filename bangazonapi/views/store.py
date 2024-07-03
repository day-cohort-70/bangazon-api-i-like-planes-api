import datetime
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from rest_framework.decorators import action
from bangazonapi.models import Store, Customer
from .product import ProductSerializer
from .paymenttype import PaymentSerializer
from .customer import CustomerSerializer
from django.contrib.auth.models import User

"""View module for handling requests about customer profiles"""

class StoreUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')

class StoreSellerSerializer(serializers.ModelSerializer):
    user = StoreUserSerializer(many=False)
    class Meta:
        model = Customer
        fields = ('id', 'user')

class StoreSerializer(serializers.HyperlinkedModelSerializer):
    seller = StoreSellerSerializer(many=False)
    products = ProductSerializer(many=True)
    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'seller', 'product_count', 'products')

class Stores(ViewSet):
    """View for interacting with customer orders"""

    # def create(self, request):
    #     new_store = Store()
    #     new_store.name = request.data["name"]
    #     new_store.description = request.data["description"]
    #     new_store.seller = Customer.objects.get(user = request.auth.user)
    #     new_store.save()

    def retrieve(self, request, pk=None):
        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store, context={'request': request})
            return Response(serializer.data)

        except Store.DoesNotExist as ex:
            return Response(
                {'message': 'The requested store does not exist, or you do not have permission to access it.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
    def list(self, request):
        """_summary_

      @api {GET} /products GET all products
        @apiName ListProducts
        @apiGroup Product

        @apiSuccess (200) {Object[]} products Array of products
        @apiSuccessExample {json} Success
            [
                {
                    "id": 101,
                    "url": "http://localhost:8000/stores",
                    "name": "",
                    "description": "It flies high",
                    "seller": {
                        "id": 1,
                        "first_name": Leah,
                        "last_name": Sanders
                    }
                    "product_count": 12
                    "products": [
                        {
                        
                        },
                        {
                        
                        }
                    ]
                }
            ]
        """
    
        stores = Store.objects.all()
            
        json_stores = StoreSerializer(
            stores, many=True, context={'request': request})

        return Response(json_stores.data)
