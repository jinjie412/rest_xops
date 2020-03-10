# -*- coding: utf-8 -*-
# @File  : login.py
# @Author: ggy
# @Date  : 2019/8/21
# @Software: PyCharm
import datetime
import uuid

# from django.contrib import auth
from graincentre.models import UserInfo

from rest_framework.views import APIView
from rest_framework.response import Response
from graincentre.models import Token


class LoginView(APIView):
    def post(self, request):
        """

        :param request:
        :return:
        """
        # 滑动验证 token 校验

        res = {"user": None, "msg": None}
        print(request.data.keys())
        try:
            # 1. 获取数据
            user = request.data.get('user')
            pwd = request.data.get('pwd')
            # print(user,pwd)
            # user_obj = auth.authenticate(username=user, password=pwd)
            user_obj = UserInfo.objects.get(username=user, password=pwd)

            if user_obj is not None:

                random_str = str(uuid.uuid4())
                Token.objects.update_or_create(user=user_obj,
                                                defaults={"key": random_str, "created": datetime.datetime.now()})
                res["user"] = user_obj.username
                res["token"] = random_str

            else:
                res["msg"] = "用户名密码错误！"


        except Exception as e:
            res["msg"] = str(e)

        return Response(res)
