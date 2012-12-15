import os
from gevent import monkey
monkey.patch_all()
import bottle

@bottle.route('/')
def index():
    return bottle.static_file('park-recs-pyramid_1500.jpg', 'public/')

bottle.run(server='gevent', port=os.environ.get('PORT', 5000))

