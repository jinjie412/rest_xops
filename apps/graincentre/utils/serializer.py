from rest_framework import serializers

from graincentre.models import OutStock, WarehousEntry


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = "__all__"
        read_only_fields = ("amount_pay", "actual_pay")

    sub_warehous_name = serializers.CharField(
        read_only=True, source='get_sub_warehous_display')
    naure_name = serializers.CharField(
        read_only=True, source='get_naure_display')
    pay_name = serializers.CharField(
        read_only=True, source='get_pay_display')
    invoice_date = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)


class SerializerCreat(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = ('voucher_number',
                  'customer_name', 'sub_warehous',
                  'mobile', 'gross_weight',
                  'vehicle_weight', 'sub_weight',
                  'unit_price', 'naure')


class SerializerPut(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = ('customer_name', 'mobile', 'gross_weight', 'vehicle_weight',
                  'sub_weight', 'net_weight', 'unit_price', 'amount_pay',
                  'pay', 'customer_get_name', 'naure')


class SerializerPutW(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = ('customer_name', 'mobile', 'gross_weight', 'vehicle_weight',
                  'sub_weight', 'unit_price',
                  'pay', 'customer_get_name', 'naure')


class SerializerOut(serializers.ModelSerializer):
    class Meta:
        model = OutStock
        fields = "__all__"

    pay_name = serializers.CharField(
        read_only=True, source='get_pay_display')
    sub_warehous_name = serializers.CharField(
        read_only=True, source='get_sub_warehous_display')
    invoice_date = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
