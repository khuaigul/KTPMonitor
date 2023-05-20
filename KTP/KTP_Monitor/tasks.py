from huey.contrib.djhuey import periodic_task
from huey import crontab
from server.contest_up import launch_all
@periodic_task(crontab(minute='*/1'))
def tasktask():
    launch_all()