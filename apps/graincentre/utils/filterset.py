from django_filters import FilterSet, DateFilter
from graincentre.models import WarehousEntry

class WarehouseEntryFilter(FilterSet):
    class Meta:
        model = WarehousEntry
        fields = '__all__'

    min_cdate = DateFilter(name='invoice_date__date', lookup_expr='gte')
    max_cdate = DateFilter(name='invoice_date__date', lookup_expr='lte')

    min_udate = DateFilter(name='update_timee__date', lookup_expr='gte')
    max_udate = DateFilter(name='update_time__date', lookup_expr='lte')

