import os
from gevent import monkey
monkey.patch_all()
import bottle

@bottle.get('/api/check')
def index():
    return "ok"

@bottle.get('/')
def index():
    return bottle.static_file('index.html', 'public/')

@bottle.get('/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, 'public/')

bottle.run(server='gevent', port=os.environ.get('PORT', 5000), host="0.0.0.0")

