from django.db.models import Sum
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from apps.common.custom import CommonPagination, RbacPermission
from apps.graincentre.utils.serializer import (
    SerializerEntryDetail, 
    SerializerEntryDetailResponse,
    SerializerEntryDetailResponseNaure, 
    SerializerEntryDetailResponseNetWeight,
    SerializerEntryDetailResponseOut,
    SerializerEntryDetailResponseNaureOut, 
    SerializerEntryDetailResponseNetWeightOut
    )
from graincentre.models import OutStock, WarehousEntry, WarehousEntryResponse
from graincentre.utils.filterset import WarehouseDetailEntryFilter, WarehouseDetailOutFilter
from rest_xops.basic import XopsResponse, XopsResponse_results


class WarehousEntryDetail(ReadOnlyModelViewSet):
    queryset = WarehousEntry.objects.all()
    serializer_class = SerializerEntryDetailResponse
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = WarehouseDetailEntryFilter
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (RbacPermission,)
    def get_serializer_class(self):
        if self.action == 'unit_price':
            return SerializerEntryDetailResponse
        elif self.action == 'net_weight':
            return SerializerEntryDetailResponseNetWeight
        elif self.action == 'naure':
            return SerializerEntryDetailResponseNaure
        elif self.action == 'pay':
            return SerializerEntryDetailResponsePay
        return SerializerEntryDetailResponse
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        r_d = request.query_params.dict()
        if 'unit_price' in r_d:
            self.action = 'unit_price'
            queryset = queryset.values("customer_name").annotate(sum_net=Sum('net_weight'), sum_amount_pay=Sum('amount_pay'), sum_actual_pay=Sum('actual_pay')).values('customer_name', 'sum_net', 'unit_price', 'sum_amount_pay', 'sum_actual_pay')
        elif 'net_weight' in r_d:
            self.action = 'net_weight'
            queryset = queryset.values("customer_name").annotate(sum_net=Sum('net_weight'), sum_amount_pay=Sum('amount_pay'), sum_actual_pay=Sum('actual_pay')).values('customer_name', 'sum_net', 'sum_amount_pay', 'sum_actual_pay')
        elif 'naure' in r_d:
            self.action = 'naure'
            queryset = queryset.values('naure').annotate(sum_net=Sum('net_weight'))
        elif 'pay' in r_d:
            self.action = 'pay'
            queryset = queryset.values('pay').annotate(sum_net=Sum('net_weight'))    
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            if self.action == 'naure':
                re_list = []
                for i in page:
                    if i['naure'] == 1:
                        re_list.append({'name': '代存', 'sum_net': i['sum_net']})
                    elif i['naure'] == 0:
                        re_list.append({'name': '收购', 'sum_net': i['sum_net']})
                return XopsResponse_results(re_list)
            else:
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class WarehousEntryDetailOut(ReadOnlyModelViewSet):
    queryset = OutStock.objects.all()
    serializer_class = SerializerEntryDetailResponseOut
    pagination_class = CommonPagination
    filter_backends = (SearchFilter, DjangoFilterBackend, OrderingFilter)
    filterset_class = WarehouseDetailOutFilter
    # authentication_classes = (JSONWebTokenAuthentication,)
    # permission_classes = (RbacPermission,)
    def get_serializer_class(self):
        if self.action == 'unit_price':
            return SerializerEntryDetailResponseOut
        elif self.action == 'net_weight':
            return SerializerEntryDetailResponseNetWeightOut
        elif self.action == 'naure':
            return SerializerEntryDetailResponseNaureOut
        return SerializerEntryDetailResponse
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        r_d = request.query_params.dict()
        if 'unit_price' in r_d:
            self.action = 'unit_price'
            queryset = queryset.values("customer_name").annotate(sum_net=Sum('net_weight'), sum_amount_pay=Sum('amount_pay'), sum_actual_pay=Sum('actual_pay')).values('customer_name', 'sum_net', 'unit_price', 'sum_amount_pay', 'sum_actual_pay')
        elif 'net_weight' in r_d:
            self.action = 'net_weight'
            queryset = queryset.values("customer_name").annotate(sum_net=Sum('net_weight'), sum_amount_pay=Sum('amount_pay'), sum_actual_pay=Sum('actual_pay')).values('customer_name', 'sum_net', 'sum_amount_pay', 'sum_actual_pay')
        elif 'naure' in r_d:
            self.action = 'naure'
            queryset = queryset.values('naure').annotate(sum_net=Sum('net_weight'))
        elif 'pay' in r_d:
            self.action = 'pay'
            queryset = queryset.values('pay').annotate(sum_net=Sum('net_weight'))    
        page = self.paginate_queryset(queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            if self.action == 'naure':
                re_list = []
                for i in page:
                    if i['naure'] == 1:
                        re_list.append({'name': '代存', 'sum_net': i['sum_net']})
                    elif i['naure'] == 0:
                        re_list.append({'name': '收购', 'sum_net': i['sum_net']})
                return XopsResponse_results(re_list)
            else:
                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
