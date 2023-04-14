from datetime import date, datetime

from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order, CommentCrm
from .forms import OrderForm
from price.models import PriceCard, PriceTable
from telebot.sendmessage import sendTelegram
from rest_framework import generics, viewsets, filters

# Create your views here.
from .serializers import OrderSerializer, CommentCrmSerializer


def first_page(request):
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    price_table = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {
        'pc_1': pc_1,
        'pc_2': pc_2,
        'pc_3': pc_3,
        'price_table': price_table,
        'form': form
    }
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    if request.POST:
        name = request.POST['name']
        phone = request.POST['phone']
        element = Order(order_name=name, order_phone=phone)
        element.save()
        sendTelegram(tg_name=name, tg_phone=phone)
        return render(request, './thanks.html', {'name': name})
    else:
        return render(request, './thanks.html')


# class OrdersAPIView(APIView):
#     def get(self, request):
#         return Response({'title': 'Статус'})


class OrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    @action(methods=["POST"], detail=True)
    def delete_order(self, request, id):
        try:
            Order.objects.get(Q(id=id)).delete()
            return Response({'message': 'success'})
        except Exception:
            return Response({'message': 'error'})

    @action(methods=['GET'], detail=True)
    def same_orders(self, request, pk):
        queryset = Order.objects.get(Q(id=pk))
        order_status = queryset.order_status
        order_name = queryset.order_dt
        same_orders = Order.objects.filter(Q(order_name=order_name) & Q(order_status=order_status))
        serializer = self.get_serializer(same_orders, many=True)
        return Response(serializer.data)


class CommentCrmAPIView(generics.ListAPIView):
    queryset = CommentCrm.objects.all()
    serializer_class = CommentCrmSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['comment_dt']
