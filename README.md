#### Ron Swanson bot

Generic twitter bot to run from heroku using python, gevent and APScheduler

You can either pay a worker dyno to run your job or keep it at it is running off a greenlet started from app.py. Change the interval by editing jobs.py.

To test locally:

- clone the repository
- cd ron_swanson_bot
- $ source env/bin/activate
- $ pip install -r
- To test locally
    create an .env file with your tweet credencials

    CONSUMER_KEY=
    CONSUMER_SECRET=
    ACCESS_TOKEN=
    ACCESS_TOKEN_SECRET=
    
    $ foreman start

- To deploy: 
    git init 
    git add .
    git commit -m 'First commit'
    heroku create appname
    git push heroku master
    heroku logs

- You can also run on Foreman/Virtualenv standalone in your server.


