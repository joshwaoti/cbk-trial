from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

from .models import (
    BasePspCustomerInfo,
    MobilePspCustomerInfo,
    MobilePsPCustomerTransactionCategorization,
    MobilePsPFailedTransactions,
    MobilePsPInteroperability
)
from .serializers import (
    MobilePspCustomerInfoSerializer,
    MobilePspCustomerTransactionCatserilizer,
    MobilePspFailedTranSerializer,
    MobilePspInterSerializer
)

class MobilePspCustomerInfoView(GenericAPIView, ListModelMixin, CreateModelMixin):
    queryset = BasePspCustomerInfo.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class MobilePspCustomerInfoDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset = BasePspCustomerInfo.objects.all()
    serializer_class = MobilePspCustomerInfoSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)