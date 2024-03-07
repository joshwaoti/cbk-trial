import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.management import call_command


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'APIs.settings')

app = Celery('APIs')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Set broker_connection_retry_on_startup to True
app.conf.broker_connection_retry_on_startup = True

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):

    sender.add_periodic_task(
        crontab(hour=9, minute=34),
        send_data_to_api.s(),
    )

@app.task
def send_data_to_api():
    call_command('send_data_to_api')

# if __name__ == '__main__':
#     app.start()