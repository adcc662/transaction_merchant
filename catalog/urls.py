from django.urls import path
from .views import CategoryListAPIView, CommerceListAPIView

urlpatterns = [
    path('categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('commerce/', CommerceListAPIView.as_view(), name='commerce-list'),
]