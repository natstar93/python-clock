import os
from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

username = os.environ.get('USERNAME')

@sched.scheduled_job('interval', minutes=3)
def timed_job():
    print('This job is run every three minutes. User {0}'.format(username))

@sched.scheduled_job('cron', day_of_week='mon-fri', hour=20)
def scheduled_job():
    print('This job is run every weekday at 8pm.')

sched.start()
