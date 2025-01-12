from rest_framework import serializers
from catalog.models import Category, Commerce

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'type']

class CommerceSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category')
    class Meta:
        model = Commerce
        fields = ['id','merchant_name', 'merchant_logo', 'category', 'category_id']
