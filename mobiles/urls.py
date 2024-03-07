from django.urls import path, include
from rest_framework import routers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="CBK API",
        default_version= "V1",
        description="This API gets data from various sources and submits them on CBK endpoints",
        terms_of_service="https://www.google.com/policies/terms",
        contact=openapi.Contact(email="contact@sniper.com"),
        license=openapi.License(name="BSD License"),
    ),
   public=True,
   permission_classes=(permissions.AllowAny,),

)


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
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path("pspcustinfo/", MobilePspCustomerInfoView.as_view()),
    path("pspcustinfo/<int:pk>/", MobilePspCustomerInfoDetailView.as_view(), name="detail"),
]
