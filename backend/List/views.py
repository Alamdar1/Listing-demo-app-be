from rest_framework import viewsets
from .models import List
from .serializer import ListSerializer  

class ListViewSet(viewsets.ModelViewSet):
    queryset = List.objects.all()
    serializer_class = ListSerializer
    