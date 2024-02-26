from django.db import models


class BasePspCustomerInfo(models.Model):
    institution_code  = models.CharField(max_length=10)
    request_id = models.CharField(max_length=10, blank=True)
    is_attached = models.CharField(max_length=1, choices=[('Y', 'Yes'), ('N', 'No')])
    reporting_date = models.DateField()

    class Meta:
        abstract = True
        unique_together = (('institution_code', 'reporting_date'),)

class MobilePspCustomerInfo(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    sub_country_code = models.CharField(max_length=4)
    gender = models.CharField(max_length=1, choices=[('M', 'Male'), ('F', 'Female')])
    age_code = models.CharField(max_length=10)
    wallet_code = models.CharField(max_length=3)
    no_of_customers_registered = models.PositiveIntegerField()
    no_of_customers_active = models.PositiveIntegerField()
    no_of_customers_inactive = models.PositiveIntegerField()
    no_of_customers_dormant = models.PositiveIntegerField()
    balances_in_customer_accts = models.DecimalField(max_digits=10, decimal_places=2)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=10, decimal_places=2)


class MobilePsPCustomerTransactionCategorization(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    sub_country_code = models.CharField(max_length=4)
    band_code = models.CharField(max_length=25)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=10, decimal_places=2)


class MobilePsPInteroperability(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    band_code = models.CharField(max_length=25)
    incoming_transaction_volume = models.PositiveIntegerField()
    incoming_transaction_value = models.DecimalField(max_digits=10, decimal_places=2)
    outgoing_transaction_volume = models.PositiveIntegerField()
    outgoing_transaction_value = models.DecimalField(max_digits=10, decimal_places=2)

class MobilePsPFailedTransactions(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    failed_transaction_code = models.CharField(max_length=8)
    band_code = models.CharField(max_length=25)
    volume_of_transactions = models.PositiveIntegerField()
    value_of_transactions = models.DecimalField(max_digits=10, decimal_places=2)
    percentage_of_failed_transactions = models.PositiveIntegerField()


class MobilePspMerchantTransactions(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    sub_country_code = models.CharField(max_length=4)
    band_code = models.CharField(max_length=25)
    merchant_id = models.CharField(max_length=10)
    merchant_type_code = models.CharField(max_length=10)
    merchant_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    merchant_classification_code = models.CharField(max_length=10)
    merchant_status = models.CharField(max_length=25)
    volume_of_deposit_transactions = models.PositiveIntegerField()
    value_of_deposit_transactions = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_withdrawal_transactions = models.PositiveIntegerField()
    value_of_withdrawal_transactions = models.DecimalField(max_digits=10, decimal_places=2)

class MobilePspMerchantCustomerBalance(BasePspCustomerInfo):
    row_id = models.IntegerField()
    psp_id = models.CharField(max_length=10)
    reporting_date = models.DateField()
    sub_country_code = models.CharField(max_length=4)
    band_code = models.CharField(max_length=25)
    merchant_id = models.CharField(max_length=10)
    merchant_type_code = models.CharField(max_length=10)
    merchant_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    merchant_classification_code = models.CharField(max_length=10)
    merchant_status = models.CharField(max_length=25)
    number_of_customers = models.PositiveIntegerField()
    end_of_day_balances = models.DecimalField(max_digits=10, decimal_places=2)