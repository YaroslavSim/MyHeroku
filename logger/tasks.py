"""Tasks."""
from celery import shared_task
from logger.models import Log

@shared_task
def delete_logs():
    """Delete logs function."""
    Log.object.all().delete()
    print("Success delete logs!")