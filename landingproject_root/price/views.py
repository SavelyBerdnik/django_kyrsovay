from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from .models import PriceTable, PriceCard
from .serializers import PriceTableSerializer, PriceCardSerializer


class PriceTableAPIView(generics.ListAPIView):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer


class PriceCardAPIView(generics.ListAPIView):
    queryset = PriceCard.objects.all()
    serializer_class = PriceCardSerializer
