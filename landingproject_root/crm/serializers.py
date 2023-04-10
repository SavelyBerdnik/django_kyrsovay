from django.contrib.auth.models import Group, User
from rest_framework import serializers
from rest_framework import serializers
from .models import Order, CommentCrm


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['order_name', 'order_phone', 'order_status']


class CommentCrmSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentCrm
        fields = ['comment_binding',  'comment_text', 'comment_dt']
