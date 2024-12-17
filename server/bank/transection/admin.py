from django.contrib import admin
from .models import UserAccountInfo,PaymantGateWay,History,TransferTempToken,AutoPay,PaymentAddress
admin.site.register(UserAccountInfo)
admin.site.register(PaymantGateWay)
admin.site.register(History)
admin.site.register(TransferTempToken)
admin.site.register(AutoPay)
admin.site.register(PaymentAddress)
