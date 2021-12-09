from django.shortcuts import render
from rest_framework import generics

# Create your views here.


from faults import models
from .serializers import FaultSerializer

class ListFault(generics.ListCreateAPIView):
    queryset = models.Faults.objects.all()
    serializer_class = FaultSerializer

class DetailFault(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Faults.objects.all()
    serializer_class = FaultSerializer