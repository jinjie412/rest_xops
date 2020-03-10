from django.db import models

# Create your models here.
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation

import datetime

class WarehousEntry(models.Model):
    '''
    入库单
    '''
    class Meta:
        verbose_name_plural = "入库单"

    voucher_number = models.CharField(max_length=14, primary_key=True, verbose_name='凭证编号')
    customer_name = models.CharField(max_length=32, verbose_name='客户名')
    mobile = models.BigIntegerField(verbose_name="手机", null=True, default='')
    sub_warehous_choices = ((1, '小麦'), (0, '玉米'))
    sub_warehous = models.SmallIntegerField(choices=sub_warehous_choices, verbose_name='仓口')
    gross_weight = models.IntegerField(verbose_name='毛重(吨)')
    vehicle_weight= models.IntegerField(verbose_name='皮重(吨)', default=0)
    net_weight = models.IntegerField(verbose_name='净重(吨)')
    sub_weight = models.IntegerField(verbose_name='扣量(吨)', null=True, blank=True)
    unit_price = models.DecimalField(max_digits=5, decimal_places=4, verbose_name='收购单价')
    amount_pay = models.DecimalField(max_digits=16, decimal_places=4, verbose_name='应付金额', null=True, blank=True)
    actual_pay = models.DecimalField(max_digits=16, decimal_places=4, verbose_name='实付金额' , null=True, blank=True)
    naure_choices = ((0, '收购'), (1, '代存'))
    naure = models.SmallIntegerField(choices=naure_choices, verbose_name='性质', default=0)
    customer_get_name = models.CharField(max_length=32, verbose_name='领取人', null=True, blank=True)
    invoice_date = models.DateTimeField('开票时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更改')

class OutStock(models.Model):
    '''
    出库单
    '''
    class Meta:
        verbose_name_plural = '出库单'
    
    voucher_number = models.CharField(max_length=14, primary_key=True, verbose_name='凭证编号')
    customer_name = models.CharField(max_length=32, verbose_name='客户名')
    mobile = models.BigIntegerField(verbose_name="手机", null=True, default='0', blank=True)
    sub_warehous_choices = ((1, '小麦'), (0, '玉米'))
    sub_warehous = models.SmallIntegerField(choices=sub_warehous_choices, verbose_name='仓口')
    gross_weight = models.IntegerField(verbose_name='毛重(吨)', null=True, blank=True)
    net_weight = models.IntegerField(verbose_name='净重(吨)', null=True, default='0', blank=True)
    vehicle_weight = models.IntegerField(verbose_name='皮重(吨)', null=True, blank=True, default=0)
    unit_price = models.DecimalField(max_digits=5, decimal_places=4, verbose_name='出库单价')
    amount_pay = models.DecimalField(max_digits=16, decimal_places=4, verbose_name='应付金额', null=True, blank=True)
    actual_pay = models.DecimalField(max_digits=16, decimal_places=4, verbose_name='实付金额', null=True, blank=True)
    invoice_date = models.DateTimeField('出库时间', auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, verbose_name='最后更改')


class Stok_All(models.Model):
    '''
    库存
    '''
    class Meta:
        verbose_name_plural = "库存"

    sub_warehous_choices = ((1, '小麦仓'), (0, '玉米仓'))
    sub_warehous = models.SmallIntegerField(choices=sub_warehous_choices, verbose_name='仓口', primary_key=True)
    entry_all = models.BigIntegerField(verbose_name='库存(吨)')
    preserve = models.BigIntegerField(verbose_name='代存(吨)', default=0)
    out_all = models.BigIntegerField(verbose_name='出库(吨)')
    now_all = models.BigIntegerField(verbose_name='余存(吨)')



class UserInfo(models.Model):
    username = models.CharField("用户名", max_length=64, unique=True)
    password = models.CharField('password', max_length=128)
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = "用户信息"

    def __str__(self):
        return self.username


class Token(models.Model):
    """
    The default authorization token model.
    """
    key = models.CharField(max_length=40)
    user = models.OneToOneField(UserInfo, related_name='auth_token', on_delete=models.CASCADE, verbose_name="关联用户")
    created = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)

    def __str__(self):
        return self.key
