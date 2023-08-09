import logging

import django_filters
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics, permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from . exceptions import ProperyNotFound
from . models import Property, PropertyViews
from . pagination import PropertyPagination
from . serializers import PropertyCreateSerializer, PropertySerializer, PropertyViewSerializer
from . filters import PropertyFilter


logger = logging.getLogger(__name__)


class ListAllPropertiesAPIView(generics.ListAPIView):
    
    serializer_class = PropertySerializer
    queryset = Property.objects.all().order_by('-created_at')
    pagination_class = PropertyPagination
    # DjangoFilterBackend integrates with django_filter and for more advanced search we use SearchFilter and OrderingFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # filterset_class for 'DjangoFilterBackend'
    filterset_class = PropertyFilter
    # search_fields for 'filters.SearchFilter' the URL query_param will be country or city
    search_fields = ['country', 'city']
    # ordering_fields for 'filters.OrderingFilter'
    ordering_fields = ['creates_at']

class ListAllPropertiesAPIView(generics.ListAPIView):

    serializer_class = PropertySerializer
    queryset = Property.objects.all().order_by('-created_at')
    pagination_class = PropertyPagination
    # DjangoFilterBackend integrates with django_filter and for more advanced search we use SearchFilter and OrderingFilter
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # filterset_class for 'DjangoFilterBackend'
    filterset_class = PropertyFilter
    # search_fields for 'filters.SearchFilter' the URL query_param will be country or city
    search_fields = ['country', 'city']
    # ordering_fields for 'filters.OrderingFilter'
    ordering_fields = ['creates_at']

    def get_queryset(self):
        user = self.request.user
        queryset = Property.objects.filter(user=user).order_by('-created_at')
        return queryset