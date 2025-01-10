import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, pagination
from .models import Keyword
from transaction.serializers import TransactionSerializer, TransactionListSerializer, KeywordSerializer
import services as transaction_services

class EnrichmentAPIView(APIView):
    def post(self, request):
        serializer = TransactionListSerializer(data={'transactions': request.data['transactions']})
        if serializer.is_valid():
            transactions = serializer.validated_data['transactions']

            enriched_transactions = metrics = transaction_services.enrich_transactions(transactions)
            created_transactions = transaction_services.created_enriched_transactions(enriched_transactions)
            response_serializer = TransactionSerializer(created_transactions, many=True)

            return Response({
                'created_transactions': response_serializer.data,
                'metrics': metrics
            }, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KeywordListAPIView(generics.ListAPIView):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer
    pagination_class = pagination.PageNumberPagination
