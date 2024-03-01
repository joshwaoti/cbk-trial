from rest_framework import serializers
from .models import BasePspCustomerInfo, MobilePspCustomerInfo, MobilePsPCustomerTransactionCategorization, MobilePsPFailedTransactions, MobilePsPInteroperability


class Serialbase(serializers.ModelSerializer):
    class Meta:
        model= MobilePspCustomerInfo
        fields = "__all__"


class MobilePspCustomerInfoSerializer(serializers.ModelSerializer):

    PspCustomerInfo = Serialbase(many=True, read_only=True)
    class Meta:
        model = BasePspCustomerInfo
        fields = ["institution_code", "request_id", "is_attached", "reporting_date", "PspCustomerInfo"]



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