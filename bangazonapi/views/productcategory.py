"""
   Author: Daniel Krusch
   Purpose: To convert product category data to json
   Methods: GET, POST
"""

"""View module for handling requests about product categories"""
from rest_framework.decorators import action
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from bangazonapi.models import ProductCategory, Product
from .product import ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductCategorySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for product category"""
    class Meta:
        model = ProductCategory
        url = serializers.HyperlinkedIdentityField(
            view_name='productcategory',
            lookup_field='id'
        )
        fields = ('id', 'url', 'name')

class ProductCategoryRecentProductsSerializer(serializers.ModelSerializer):

    recent_products = serializers.SerializerMethodField()
    def get_recent_products(self,obj):
        recent_products = Product.objects.filter(category=obj).order_by('-created_date')[:5]
        serializer = ProductSerializer(recent_products, many=True, context=self.context)
        return serializer.data

    class Meta:
        model = ProductCategory
        fields = ('id','name','recent_products')


class ProductCategories(ViewSet):
    """Categories for products"""
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized product category instance
        """
        new_product_category = ProductCategory()
        new_product_category.name = request.data["name"]
        new_product_category.save()

        serializer = ProductCategorySerializer(new_product_category, context={'request': request})

        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single category"""
        try:
            category = ProductCategory.objects.get(pk=pk)
            serializer = ProductCategorySerializer(category, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to ProductCategory resource"""
        product_category = ProductCategory.objects.all()

        # Support filtering ProductCategorys by area id
        # name = self.request.query_params.get('name', None)
        # if name is not None:
        #     ProductCategories = ProductCategories.filter(name=name)

        serializer = ProductCategorySerializer(
            product_category, many=True, context={'request': request})
        return Response(serializer.data)

    @action(methods=['get'], detail=False)
    def recentproducts(self, request):

        if request.method == "GET":
            
            product_categories = ProductCategory.objects.all()
            serializer = ProductCategoryRecentProductsSerializer(product_categories, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)


        