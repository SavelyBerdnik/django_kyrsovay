from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PriceTable, PriceCard
from .serializers import PriceTableSerializer, PriceCardSerializer


class PriceTableAPIView(generics.ListAPIView):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer


class PriceTableViewSet(viewsets.ModelViewSet):
    queryset = PriceTable.objects.all()
    serializer_class = PriceTableSerializer

    @action(methods=["GET"], detail=False)
    def list_price(self, request):
        queryset = PriceTable.objects.order_by('-id')
        serializer = self.get_serializer(queryset, many=True)
        paginator = Paginator(queryset, per_page=3)
        return Response(serializer.data)


class PriceCardAPIView(generics.ListAPIView):
    queryset = PriceCard.objects.all()
    serializer_class = PriceCardSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['pc_value']
