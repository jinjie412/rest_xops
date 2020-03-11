from rest_framework.views import APIView
from rest_framework.response import Response

from decimal import Decimal
from datetime import datetime
import random
import string

from graincentre.utils.response import BaseResponse
from graincentre.utils.exceptions import CommonException
from graincentre.utils.serializer import Serializer, SerializerPut
from graincentre.models import Stok_All, WarehousEntry
from graincentre.utils.paginates import Pagination

from rest_xops.basic import XopsResponse_results


class WarehousEntryView(APIView):
    '''
    入库
    '''

    def post(self, request):
        msg = '''
        {
            "customer_name": 客户名,
            "sub_warehous": 仓口,
            "gross_weight": 毛重, 
            "vehicle_weight": 皮重, 
            "sub_weight": 扣量, 
            "unit_price": 单价, 
            "naure": 性质
        }

        '''
        res = BaseResponse()
        get_data_set = {'customer_name', 'sub_warehous',
                        'gross_weight', 'vehicle_weight', 'sub_weight', 'unit_price', 'naure'}
        try:
            if get_data_set.issubset(set(request.data.keys())):
                rd = ''.join(random.sample(string.digits, 2))
                request.data['voucher_number'] = datetime.now().strftime(
                    "%Y%m%d%H%M") + rd
                # print(request.data)
                gross_weight = request.data['gross_weight']
                net_weight = gross_weight - \
                    request.data['vehicle_weight'] - request.data['sub_weight']
                if net_weight < 0:
                    raise CommonException('净重结果是负数,输入异常', 1003)
                
                request.data['net_weight'] = net_weight
                request.data['amount_pay'] = Decimal(
                    net_weight) * Decimal(request.data['unit_price'])
                verified_data = Serializer(data=request.data, many=False)
                if verified_data.is_valid():
                    verified_data.save()
                    return Response(verified_data.data)
                else:
                    raise CommonException('序列化失败', 1002)
            else:
                raise CommonException("数据不完整: ", 1001)

        except CommonException as e:
            res.code = e.code
            res.msg = e.msg

        return Response(res.dict)

    def get(self, request):
        sub_warehous = request.query_params.get('sub_warehous')
        warehous_entry = WarehousEntry.objects.filter(
            sub_warehous=sub_warehous).order_by('-invoice_date')
        paginater = Pagination()
        pagewarehous_entry = paginater.paginate_queryset(
            warehous_entry, request)
        serialized_data = Serializer(pagewarehous_entry, many=True)
        return XopsResponse_results(serialized_data.data)

    def put(self, request, pk):
        res = BaseResponse()
        get_data_set = {'voucher_number', 'customer_name', 'actual_pay', 'gross_weight', 'vehicle_weight', 'sub_weight', 'unit_price', 'naure'}
                        
        try:
            if get_data_set.issubset(set(request.data.keys())):
                put_obj = WarehousEntry.objects.get(voucher_number=pk)
                #数据处理
                if request.data['unit_price'] == "0.0000":
                    request.data['unit_price'] = 0             

                gross_weight = request.data['gross_weight']
                net_weight = gross_weight - \
                    request.data['vehicle_weight'] - request.data['sub_weight']
                if net_weight < 0:
                    raise CommonException('净重结果是负数,输入异常', 1003)
                
                request.data['net_weight'] = net_weight
                request.data['amount_pay'] = Decimal(
                    net_weight) * Decimal(request.data['unit_price'])
                verified_data = SerializerPut(data=request.data, instance=put_obj, many=False)
                if verified_data.is_valid():
                    verified_data.save()
                    return XopsResponse_results(verified_data.data)
                else:
                    print(verified_data.data)
                    raise CommonException('序列化失败', 1002)
            else:
                raise CommonException("数据不完整: ", 1001)

        except CommonException as e:
            res.code = e.code
            res.msg = e.msg

        return XopsResponse_results(res.dict, msg=res.msg)

    def delete(self, request, pk):
        WarehousEntry.objects.get(pk=pk).delete()
        return Response()
