import gevent
import twitter
from apscheduler.scheduler import Scheduler

from gevent import monkey
monkey.patch_all()

sched = Scheduler()

f = open('public/quotes.txt', 'r') 
quotes = f.readlines()

@sched.cron_schedule(minutes=45)
def send_random_message():
    pass

@sched.cron_schedule(minutes=10)
def filter_stream_and_reply():
    pass

sched.start()

while True:
    pass

