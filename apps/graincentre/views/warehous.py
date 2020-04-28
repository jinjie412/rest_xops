
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
import time


class Warehous(ModelViewSet):
    queryset = WarehousEntry.objects.all()
    serializer_class = Serializer
    pagination_class = CommonPagination

    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filterset_fields = ('naure', 'sub_warehous')

    filterset_class = WarehouseEntryFilter
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
        serializer.validated_data['net_weight'] = serializer.validated_data['net_weight'] *2
        if serializer.validated_data['net_weight'] < 0:
            return XopsResponse('净重结果是负数,输入异常')
        
        if serializer.validated_data['naure'] == 1:#代存
            serializer.validated_data['amount_pay'] = 0
            serializer.validated_data['unit_price'] = 0
        elif serializer.validated_data['naure'] == 0:
            serializer.validated_data['amount_pay'] = Decimal(
                serializer.validated_data['net_weight']) * Decimal(request.data['unit_price'])
        else:
            return XopsResponse('naure error')
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return XopsResponse(serializer.data, status=CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        msg = '修改成功'
        print(request.data)
        print(kwargs)
        put_obj = WarehousEntry.objects.get(voucher_number=kwargs['pk'])
        serializer = self.get_serializer(data=request.data, instance=put_obj, many=False)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['net_weight'] = request.data['gross_weight'] - \
            request.data['vehicle_weight'] - request.data['sub_weight']
        serializer.validated_data['net_weight'] = serializer.validated_data['net_weight'] *2
        if serializer.validated_data['net_weight'] < 0:
            return XopsResponse('净重结果是负数,输入异常')
        
        if serializer.validated_data['net_weight'] < 0:
            return XopsResponse('净重结果是负数,输入异常')
        
        if serializer.validated_data['naure'] == 1: #代存
            serializer.validated_data['amount_pay'] = 0
            serializer.validated_data['amount_pay'] = 0
            serializer.validated_data['actual_pay'] = 0
        elif serializer.validated_data['naure'] == 0:#收购
            serializer.validated_data['amount_pay'] = Decimal(
                serializer.validated_data['net_weight']) * Decimal(request.data['unit_price'])

        else:
            msg = 'naure error'
            return XopsResponse(msg=msg)

        if 1 == serializer.validated_data['pay'] and 0 == serializer.validated_data['naure']:
            if serializer.validated_data['unit_price'] == 0:
                msg = "代存订单需要设定收购单价,才能付款"
                serializer.validated_data['actual_pay'] = 0
                serializer.validated_data['pay'] = 0
            else:
                serializer.validated_data['actual_pay'] = serializer.validated_data['amount_pay']
                msg = "付款成功"
        elif 1 == serializer.validated_data['pay'] and 1 == serializer.validated_data['naure']:
            serializer.validated_data['pay'] = 0
            msg = "代存订单不能结账付款,修改为收购,设定单价在付款"
        else:
            serializer.validated_data['actual_pay'] = 0
            msg = "设定欠账,已付款清零"

        self.perform_update(serializer)
        print(serializer.data)
        return XopsResponse(serializer.data, msg=msg)

