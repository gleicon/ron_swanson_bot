import random
import os
import gevent
import twitter
from apscheduler.scheduler import Scheduler
from pymongo import Connection
from gevent import monkey
monkey.patch_all()

sched = Scheduler()
api = twitter.Api(consumer_key=os.environ['CONSUMER_KEY'],
        consumer_secret=os.environ['CONSUMER_SECRET'],
        access_token_key=os.environ['ACCESS_TOKEN'],
        access_token_secret=os.environ['ACCESS_TOKEN_SECRET'])

pyramid={}

f = open('public/quotes.txt', 'r') 
quotes = f.readlines()
f.close()

f=open('public/pyramid.txt', 'r')
a=f.readlines()
f.close()

quotes = quotes + a

@sched.interval_schedule(minutes=1)
def send_random_message():
    t = api.PostUpdate(random.choice(quotes).strip())
    print "random message posted: %s" % t

sched.start()

