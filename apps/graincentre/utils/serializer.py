from rest_framework import serializers

from graincentre.models import WarehousEntry, OutStock

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = WarehousEntry
        fields = "__all__"
    
    sub_warehous_name = serializers.CharField(read_only=True, source='get_sub_warehous_display')
    naure_name = serializers.CharField(read_only=True, source='get_naure_display')
    invoice_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)


class SerializerOut(serializers.ModelSerializer):
    class Meta:
        model = OutStock
        fields = "__all__"
    
    sub_warehous_name = serializers.CharField(read_only=True, source='get_sub_warehous_display')
    invoice_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
    update_time = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False, read_only=True)
	