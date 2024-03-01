# Generated by Django 5.0.2 on 2024-02-26 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilepspcustomerinfo',
            name='base_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PspCustomerInfo', to='mobiles.basepspcustomerinfo'),
        ),
    ]