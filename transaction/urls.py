from django.urls import path
from .views import EnrichmentAPIView, KeywordListAPIView

urlpatterns = [
    path('enrichment/', EnrichmentAPIView.as_view(), name='enrichment'),
    path('keywords/', KeywordListAPIView.as_view(), name='keyword-list'),
]