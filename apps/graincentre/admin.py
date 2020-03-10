from django.contrib import admin

from .models import WarehousEntry, OutStock, Stok_All, UserInfo, Token


@admin.register(WarehousEntry)
class WarehousEntryAdmin(admin.ModelAdmin):
    list_display = ['id', 'voucher_number', 'customer_name', 'mobile', 'sub_warehous', 'gross_weight', 'vehicle_weight', 'sub_weight', 'net_weight',
                    'unit_price', 'amount_pay', 'actual_pay', 'naure', 'customer_get_name', 'invoice_date', 'update_time']
    list_filter = ['voucher_number', 'invoice_date', 'naure', 'customer_name',
                   'mobile', 'sub_warehous', 'customer_get_name', 'update_time']


@admin.register(OutStock)
class OutStockAdmin(admin.ModelAdmin):
    list_display = ['id', 'voucher_number', 'customer_name', 'mobile', 'sub_warehous', 'gross_weight', 'vehicle_weight', 'net_weight',
                    'unit_price', 'amount_pay', 'actual_pay', 'invoice_date', 'update_time']
    list_filter = ['voucher_number', 'invoice_date',
                   'customer_name', 'mobile', 'sub_warehous', 'update_time']


@admin.register(Stok_All)
class Stok_AllAdmin(admin.ModelAdmin):
    list_display = ['sub_warehous', 'entry_all',
                    'preserve', 'out_all', 'now_all']
    list_filter = []


@admin.register(UserInfo)
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']


@admin.register(Token)
class TokenAdmin(admin.ModelAdmin):
    list_display = ['key', 'user', 'created']
