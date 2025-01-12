from rest_framework import generics, pagination
from .models import Category, Commerce
from .serializers import CategorySerializer, CommerceSerializer


class CategoryListAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = pagination.PageNumberPagination

class CommerceListAPIView(generics.ListCreateAPIView):
    queryset = Commerce.objects.all()
    serializer_class = CommerceSerializer
    pagination_class = pagination.PageNumberPagination

