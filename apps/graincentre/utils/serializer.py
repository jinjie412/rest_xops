from rest_framework import serializers

from graincentre.models import OutStock, WarehousEntry, WarehousEntryResponse


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

class SerializerEntryDetail(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = ('sub_warehous', 'invoice_date')
        extra_kwargs = {
            'sub_warehous': {
                'required': True,
                'error_messages': {
                    'required': '必填项',
                }
            },
        } 

class SerializerEntryDetailResponse(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = '__all__'

class SerializerEntryDetailResponseNetWeight(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'customer_name', 'sum_amount_pay', 'sum_actual_pay')

class SerializerEntryDetailResponseNaure(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'naure')
    
class SerializerEntryDetailResponsePay(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'pay')

class SerializerEntryDetailResponseOut(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = '__all__'

class SerializerEntryDetailResponseNetWeightOut(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'customer_name', 'sum_amount_pay', 'sum_actual_pay')

class SerializerEntryDetailResponseNaureOut(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'naure')
    
class SerializerEntryDetailResponsePayOut(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntryResponse
        fields = ('sum_net', 'pay')

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


