import random
import logging
import os
import gevent
import twitter
from apscheduler.scheduler import Scheduler

from gevent import monkey
monkey.patch_all()

sched = Scheduler()
api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        access_token_key=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

f = open('public/quotes.txt', 'r') 

quotes = f.readlines()

@sched.interval_schedule(minutes=1)
def send_random_message():
    t = api.PostUpdate(random.choice(quotes).strip())
    logging.info("random message posted: %s" % t)

@sched.interval_schedule(minutes=20)
def filter_stream_and_reply():
    pass

sched.start()

while True:
    pass

