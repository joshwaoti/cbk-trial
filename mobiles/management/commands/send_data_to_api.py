from django.core.management.base import BaseCommand
from mobiles.models import BasePspCustomerInfo
import requests
import csv
from io import StringIO

class Command(BaseCommand):
    help = 'Send data to another API daily at 22:00'

    def handle(self, *args, **kwargs):
        url = 'https://eoc0vud0ipdzj1h.m.pipedream.net'
        data_list = BasePspCustomerInfo.objects.all().values()

        # Create a CSV string from the data
        csv_data = StringIO()
        csv_writer = csv.DictWriter(csv_data, fieldnames=data_list[0].keys())
        csv_writer.writeheader()
        csv_writer.writerows(data_list)

        # Reset the CSV string to be read from the beginning
        csv_data.seek(0)

        # Send data in CSV format
        response = requests.post(url, data=csv_data)

        if response.status_code == 200:
            self.stdout.write(self.style.SUCCESS(f'Successfully sent data to API'))
        else:
            self.stdout.write(self.style.ERROR(f'Failed to send data to API'))
