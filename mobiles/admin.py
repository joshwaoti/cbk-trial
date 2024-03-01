from django.contrib import admin
from .models import BasePspCustomerInfo, MobilePspCustomerInfo

admin.site.register(BasePspCustomerInfo)
admin.site.register(MobilePspCustomerInfo)