# Generated by Django 5.0.3 on 2024-03-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobiles', '0002_alter_mobilepspcustomerinfo_base_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mobilepspcustomerinfo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('C', 'Cooperate'), ('O', 'Others')], max_length=1),
        ),
    ]
