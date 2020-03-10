from rest_framework.views import APIView
from rest_framework.response import Response

from decimal import Decimal
from datetime import datetime
import random
import string

from graincentre.utils.response import BaseResponse
from graincentre.utils.exceptions import CommonException
from graincentre.utils.serializer import SerializerOut
from graincentre.models import Stok_All, OutStock
from graincentre.utils.paginates import Pagination


class OutStockView(APIView):
    '''
    入库
    '''

    def post(self, request):
        msg = '''{"customer_name": "客户名","sub_warehous": "仓口(0,1)","gross_weight": "毛重","vehicle_weight": "皮重", "unit_price": "单价"}'''
        res = BaseResponse()
        get_data_set = {'customer_name', 'sub_warehous',
                        'gross_weight', 'vehicle_weight', 'unit_price'}
        try:
            if get_data_set.issubset(set(request.data.keys())):
                verified_data = SerializerOut(data=request.data, many=False)
                print('request.data: ', request.data)
                if verified_data.is_valid():
                    net_weight = request.data['gross_weight'] - request.data['vehicle_weight']
                    if net_weight < 0:
                        raise CommonException('净重结果小于 0; 毛重,皮重数据输入错误', 1003)
                    rd = ''.join(random.sample(string.digits, 2))
                    verified_data.validated_data['voucher_number'] = datetime.now().strftime(
                        "%Y%m%d%H%M") + rd
                    verified_data.validated_data['net_weight'] = net_weight
                    verified_data.validated_data['amount_pay'] = Decimal(
                        net_weight) * Decimal(request.data['unit_price'])
                    stok_obj = Stok_All.objects.get(
                        sub_warehous=verified_data.validated_data['sub_warehous'])
                    stok_obj.out_all = stok_obj.out_all + net_weight

                    if stok_obj.entry_all + stok_obj.preserve < stok_obj.out_all:
                        raise CommonException('出库数量大于库存数量', 1004)

                    stok_obj.now_all = stok_obj.entry_all + stok_obj.preserve - stok_obj.out_all
                    stok_obj.save()
                    verified_data.save()
                    return Response(verified_data.data)
                else:
                    print(verified_data.data)
                    raise CommonException('序列化失败', 1002)
            else:
                raise CommonException("数据不完整: "+msg, 1001)

        except CommonException as e:
            res.code = e.code
            res.msg = e.msg

        return Response(res.dict)

    def get(self, request):
        warehous_entry = OutStock.objects.all()
        paginater = Pagination()
        pagewarehous_entry = paginater.paginate_queryset(
            warehous_entry, request)
        serialized_data = SerializerOut(pagewarehous_entry, many=True)
        return Response(serialized_data.data)
