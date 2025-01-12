from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from catalog.models import Commerce
from catalog.serializers import CategorySerializer, CommerceSerializer
from .models import Transaction, Keyword
import uuid
from datetime import datetime

class TransactionInputSerializer(serializers.Serializer):
    id = serializers.UUIDField()
    description = serializers.CharField()
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    date = serializers.DateField()

    def to_internal_value(self, data):
        if 'id' in data:
            try:
                data['id'] = uuid.UUID(data['id'])
            except ValueError:
                raise ValidationError({'id': 'Invalid UUID format.'})
        else:
            data['id'] = None

        try:
            data['amount'] = float(data['amount'])
        except ValueError:
            raise ValidationError({'amount': 'Invalid amount format.'})

        try:
            data['date'] = datetime.strptime(data['date'], '%Y-%m-%d').date()
        except ValueError:
            raise ValidationError({'date': 'Invalid date format.'})

        return super().to_internal_value(data)

class TransactionListSerializer(serializers.Serializer):
    transactions = serializers.ListSerializer(child=TransactionInputSerializer())

class TransactionSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    merchant = CommerceSerializer()

    class Meta:
        model = Transaction
        fields = ['id', 'description', 'amount', 'date', 'category', 'merchant', 'created_at', 'updated_at']

class KeywordSerializer(serializers.ModelSerializer):
    merchant_id = serializers.PrimaryKeyRelatedField(
        queryset=Commerce.objects.all(), source='merchant'
    )
    class Meta:
        model = Keyword
        fields = ['id', 'keyword', 'merchant_id']