from rest_framework.views import APIView
from rest_framework.response import Response

from decimal import Decimal
from datetime import datetime
import random
import string

from graincentre.utils.response import BaseResponse
from graincentre.utils.exceptions import CommonException
from graincentre.utils.serializer import Serializer
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
        pop_data = {"amount_pay", "actual_pay"}
        try:
            if get_data_set.issubset(set(request.data.keys())):
                for v in pop_data:
                    if v in request.data:
                        request.data.pop(v)

                rd = ''.join(random.sample(string.digits, 2))
                request.data['voucher_number'] = datetime.now().strftime(
                    "%Y%m%d%H%M") + rd
                # print(request.data)
                gross_weight = request.data['gross_weight']
                net_weight = gross_weight - \
                    request.data['vehicle_weight'] - request.data['sub_weight']
                if net_weight < 0:
                    raise CommonException('净重结果是负数,输入异常', 1003)

                verified_data = Serializer(data=request.data, many=False)
                if verified_data.is_valid():

                    verified_data.validated_data['net_weight'] = net_weight
                    verified_data.validated_data['amount_pay'] = Decimal(
                        net_weight) * Decimal(request.data['unit_price'])
                    # stok_obj = Stok_All.objects.get(
                    #     sub_warehous=verified_data.validated_data['sub_warehous'])

                    # if verified_data.validated_data['naure'] == 1:
                    #     # 代存
                    #     stok_obj.preserve = stok_obj.preserve + \
                    #         request.data['net_weight']
                    # else:
                    #     stok_obj.entry_all = stok_obj.entry_all + \
                    #         request.data['net_weight']

                    # stok_obj.now_all = stok_obj.entry_all + stok_obj.preserve - stok_obj.out_all
                    # stok_obj.save()
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
        print(sub_warehous)
        warehous_entry = WarehousEntry.objects.filter(
            sub_warehous=sub_warehous).order_by('-invoice_date')
        paginater = Pagination()
        pagewarehous_entry = paginater.paginate_queryset(
            warehous_entry, request)
        serialized_data = Serializer(pagewarehous_entry, many=True)
        return XopsResponse_results(serialized_data.data)

    def put(self, request):
        res = BaseResponse()
        print(request.data)
        get_data_set = {'voucher_number', 'customer_name', 'actual_pay', 'gross_weight', 'vehicle_weight', 'sub_weight', 'unit_price', 'naure'}
                        
        pop_data = {"amount_pay", "invoice_date", "update_time"}
        print(set(request.data.keys()))
        try:
            if get_data_set.issubset(set(request.data.keys())):
                for v in pop_data:
                    if v in request.data:
                        request.data.pop(v)

                put_obj = WarehousEntry.objects.get(request.data[''])
                gross_weight = request.data['gross_weight']
                net_weight = gross_weight - \
                    request.data['vehicle_weight'] - request.data['sub_weight']
                if net_weight < 0:
                    raise CommonException('净重结果是负数,输入异常', 1003)

                verified_data = Serializer(data=request.data, many=False)
                if verified_data.is_valid():

                    verified_data.validated_data['net_weight'] = net_weight
                    verified_data.validated_data['amount_pay'] = Decimal(
                        net_weight) * Decimal(request.data['unit_price'])
                    verified_data.update()
                    return XopsResponse_results(verified_data.data)
                else:
                    raise CommonException('序列化失败', 1002)
            else:
                raise CommonException("数据不完整: ", 1001)

        except CommonException as e:
            res.code = e.code
            res.msg = e.msg

        return XopsResponse_results(res.dict, msg=res.msg)
