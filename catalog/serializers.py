from rest_framework import serializers
from catalog.models import Category, Commerce

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = []

class CommerceSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Commerce
        fields = ['id','merchant_name', 'merchant_logo', 'category']
