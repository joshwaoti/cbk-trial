from django.urls import path, include
from rest_framework import routers

from .views import (
    MobilePspCustomerInfoView,
    MobilePspCustomerInfoDetailView,
)


# router =routers.DefaultRouter()
# router.register(r'pspcustinfo', MobilePspCustomerInfoView, basename='mobile-psp-customer-info')


# urlpatterns = [
#     path("", include(router.urls))
# ]

urlpatterns = [
    path("pspcustinfo/", MobilePspCustomerInfoView.as_view()),
    path("pspcustinfo/<int:pk>/", MobilePspCustomerInfoDetailView.as_view(), name="detail"),
]
