from rest_framework import serializers
from .models import PriceTable, PriceCard


class PriceTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceTable
        fields = ['pt_title', 'pt_old_price', 'pt_new_price']


class PriceCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = PriceCard
        fields = ['pc_value', 'pc_description']
