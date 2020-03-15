from django_filters import FilterSet, DateFilter, NumberFilter, CharFilter
from graincentre.models import WarehousEntry, OutStock


class WarehouseEntryFilter(FilterSet):
    min_net_weight = NumberFilter(field_name='net_weight', lookup_expr='gte')
    max_net_weight = NumberFilter(field_name='net_weight', lookup_expr='lte')

    min_cdate = DateFilter(field_name='invoice_date', lookup_expr='gte')
    max_cdate = DateFilter(field_name='invoice_date', lookup_expr='lte')

    min_udate = DateFilter(field_name='update_time', lookup_expr='gte')
    max_udate = DateFilter(field_name='update_time', lookup_expr='lte')

    naure = NumberFilter(field_name='naure')
    pay = NumberFilter(field_name='pay')
    sub_warehous = CharFilter(field_name='sub_warehous')

    class Meta:
        model = WarehousEntry
        fields = ['sub_warehous', 'naure', 'pay', 'min_net_weight', 'max_net_weight',
                  'min_cdate', 'max_cdate', 'min_udate', 'max_udate']


class WarehouseDetailEntryFilter(FilterSet):
    min_cdate = DateFilter(field_name='invoice_date', lookup_expr='gte')
    max_cdate = DateFilter(field_name='invoice_date', lookup_expr='lte')

    min_udate = DateFilter(field_name='update_time', lookup_expr='gte')
    max_udate = DateFilter(field_name='update_time', lookup_expr='lte')
    class Meta:
        model = WarehousEntry
        fields = ['sub_warehous', 'min_cdate', 'max_cdate', 'min_udate', 'max_udate']



class WarehouseDetailOutFilter(FilterSet):
    min_cdate = DateFilter(field_name='invoice_date', lookup_expr='gte')
    max_cdate = DateFilter(field_name='invoice_date', lookup_expr='lte')

    min_udate = DateFilter(field_name='update_time', lookup_expr='gte')
    max_udate = DateFilter(field_name='update_time', lookup_expr='lte')
    class Meta:
        model = OutStock
        fields = ['sub_warehous', 'min_cdate', 'max_cdate', 'min_udate', 'max_udate']