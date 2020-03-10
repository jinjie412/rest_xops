
import random
import string
from datetime import datetime
from decimal import Decimal

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.viewsets import ModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.common.custom import CommonPagination, RbacPermission
from graincentre.models import WarehousEntry
from graincentre.utils.filterset import WarehouseEntryFilter
from apps.graincentre.utils.paginates import Pagination
from apps.graincentre.utils.serializer import (Serializer, SerializerCreat,
                                               SerializerPut)
from rest_xops.basic import XopsResponse
from rest_xops.code import *


class Warehous(ModelViewSet):
    queryset = WarehousEntry.objects.all()
    serializer_class = Serializer
    pagination_class = CommonPagination
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = ('naure',)
    # filter_class = WarehouseEntryFilter
    search_fields = ('=voucher_number', 'customer_name', 'mobile')
    ordering_fields = ('invoice_date',)
    authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = (RbacPermission,)

    def get_serializer_class(self):
        if self.action == 'update':
            return SerializerPut
        elif self.action == 'creat':
            return SerializerCreat
        return Serializer

    def create(self, request, *args, **kwargs):
        rd = ''.join(random.sample(string.digits, 2))
        request.data['voucher_number'] = datetime.now().strftime(
            "%Y%m%d%H%M") + rd
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['net_weight'] = request.data['gross_weight'] - \
            request.data['vehicle_weight'] - request.data['sub_weight']
        if serializer.validated_data['net_weight'] < 0:
            return XopsResponse('净重结果是负数,输入异常')
        serializer.validated_data['amount_pay'] = Decimal(
            serializer.validated_data['net_weight']) * Decimal(request.data['unit_price'])
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return XopsResponse(serializer.data, status=CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        put_obj = WarehousEntry.objects.get(voucher_number=kwargs['pk'])
        serializer = self.get_serializer(data=request.data, instance=put_obj, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['net_weight'] = request.data['gross_weight'] - \
            request.data['vehicle_weight'] - request.data['sub_weight']
        if serializer.validated_data['net_weight'] < 0:
            return XopsResponse('净重结果是负数,输入异常')
        serializer.validated_data['amount_pay'] = Decimal(
            serializer.validated_data['net_weight']) * Decimal(request.data['unit_price'])
        self.perform_update(serializer)
        return XopsResponse('ppp')
