from django.shortcuts import render
from newsappAPI.constants import item_url, max_id_url
from rest_framework.decorators import api_view
from rest_framework import status, generics
from .hackernewsapi import get_latest_news, update_news
from rest_framework.response import Response
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter, SearchFilter
import requests
from .models import Item
from .serializers import ItemSerializer
from django.http import Http404
from concurrent.futures import ThreadPoolExecutor
import concurrent



# Create your views here.

class ItemsView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    ordering_fields = ['title', 'time']
    filterset_fields = ['type']
    search_fields = ['title', 'text']

    def perform_create(self, serializer):
        serializer.save(source='API')

class ItemsManagerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_object(self):
        try:
            pk = self.kwargs.get('pk')
            item = Item.objects.get(id=pk)
            return item
        except Item.DoesNotExist:
            raise Http404

    def patch(self, request, *args, **kwargs):
        data = {}
        item = Item.objects.get(pk=kwargs.get('pk'))
        if item.source == 'API':
            return self.partial_update(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        item = Item.objects.get(pk=kwargs.get('pk'))
        if item.source == 'API':
            self.destroy(request, *args, **kwargs)

        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['GET'])
def latest_news(request):
    data = update_news()

    return Response(data)
