from celery import Celery
from celery.schedules import crontab
from django.conf import settings
from django.core.management import call_command

app = Celery('APIs')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=8, minute=17),
        send_data_to_api.s(),
    )

@app.task
def send_data_to_api():
    call_command('send_data_to_api')
