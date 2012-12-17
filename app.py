import os
import gevent
from gevent import monkey
monkey.patch_all()
import bottle
import jobs

q = None

@bottle.get('/api/check')
def index():
    return "ok"

@bottle.get('/api/quote')
def index():
    return jobs.random_quote(q)

@bottle.get('/')
def index():
    return bottle.static_file('index.html', 'public/')

@bottle.post('/fb')
def fb():
    return bottle.static_file('fb-canvas.html', 'public/')

@bottle.get('/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, 'public/')

if __name__ == '__main__':
    print "Loading quotes"
    q = jobs.load_quotes()
    print "Spawning scheduler"
    gevent.spawn(jobs.initialize, q)
    print "Running Bottle"
    bottle.run(server='gevent', port=os.environ.get('PORT', 5000), host="0.0.0.0")

