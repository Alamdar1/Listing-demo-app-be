from rest_framework import viewsets
from .models import List
from django_filters.rest_framework import DjangoFilterBackend

from .serializer import ListSerializer  

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    filter_backends = [DjangoFilterBackend]  # enable filter backend

    filterset_fields = ['title', 'price', 'location']  # list of fields you want to filter
