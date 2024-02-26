from rest_framework import serializers
from .models import MobilePspCustomerInfo, MobilePsPCustomerTransactionCategorization, MobilePsPFailedTransactions, MobilePsPInteroperability

class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePspCustomerInfo
        fields = "__all__"


class MobilePspCustomerTransactionCatserilizer(serializers.ModelSerializer):
    class Meta:
        model = MobilePsPCustomerTransactionCategorization
        fields = "__all__"


class MobilePspFailedTranSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePsPFailedTransactions
        fields = "__all__"


class MobilePspInterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePsPInteroperability
        fields = "__all__"