#### Ron Swanson bot

Generic twitter bot to run from heroku using python, gevent and APScheduler. It also has an example facebook application to authorize and post quotes to your timeline. All in the same process. Using canvas. Greatness achieved.

You can either pay a worker dyno to run your job or keep it at it is running off a greenlet started from app.py. Change the interval by editing jobs.py. Run jobs.py in a different process if you want.

To test locally:

- you will need foreman, virtualenv, etc, etc
- clone the repository
- cd ron_swanson_bot
- $ virtualenv --no-site-packages env
- $ source env/bin/activate
- $ pip install -r requirements.txt
- To test locally
    create an .env file with your tweet credencials using the following env vars:

    - CONSUMER_KEY=
    - CONSUMER_SECRET=
    - ACCESS_TOKEN=
    - ACCESS_TOKEN_SECRET=
    - FB_APP_ID=
    - FB_APP_SECRET=

    run with:

    $ foreman start

- To deploy: 
    git init 
    git add .
    git commit -m 'First commit'
    heroku create appname
    git push heroku master
    heroku config:add CONSUMER_KEY= CONSUMER_SECRET= ACCESS_TOKEN= ACCESS_TOKEN_SECRET= FB_APP_ID= FB_APP_SECRET=
    heroku logs

- You can also run on Foreman/Virtualenv standalone in your server.


