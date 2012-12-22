import os
import gevent
from gevent import monkey
monkey.patch_all()
import bottle
import jobs

q = None

def get_fb_user_graph(request):
    user = facebook.get_user_from_cookie(request.cookies, os.environ.get('FB_APP_ID'), os.environ.get('FB_APP_SECRET')) 
    if not user: return None

    graph = facebook.GraphAPI(user['access_token']).get_object("me")
    graph['uid'] = user['uid']

    return graph    

@bottle.get('/api/check')
def index():
    return "ok"

@bottle.get('/api/quote')
def index():
    return jobs.random_quote(q)

@bottle.get('/fb')
def febe():
    return bottle.template('public/fb-canvas.html', fb_app_id=os.environ.get('FB_APP_ID'))

@bottle.get('/')
def index():
    return bottle.static_file('index.html', 'public/')

@bottle.post('/fb')
def fb():
    return bottle.template('public/fb-canvas.html', fb_app_id=os.environ.get('FB_APP_ID'))

@bottle.post('/api/fb/timeline')
def fb_post():
    pass

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

