#################################### READ THE DOCS, PLEBS ###################################################
## Dependency Docs:                                                                                        ##
##   Flask:  Micro webdevelopment framework             - http://flask.pocoo.org/docs/                     ##
##   FlaskRedis: Adds Redis support to Flask.           - https://github.com/underyx/flask-redis           ##
##   Redis-Py: Redis Interface. Used by FlaskRedis      - https://github.com/andymccurdy/redis-py          ##
######################################### THANK YOU, FRIEND #################################################


#################################### BLANK SLATE, LETS GET SOME STUFF #######################################
import sys, json                                        # I never leave home without it
REDIS_URL = "redis://localhost:6379/0"                  # Where to, buddy?  Ah I see, so you want your redis server.
                                                        # No problem, but its dangerous out there.  Take these:
from flask import Flask, jsonify                        #  First, my Flask.  It will be the bottle for your ship.
from flask_redis import FlaskRedis                      #  Here's an enhancement for your Flask, it provides Redis.
from redis import Redis                                 #  Get regular Redis interface too, just in case for hashes
#############################################################################################################



#################################### OK FAM, LETS GET TO WORK ###############################################
app = Flask(__name__)                                   # 1. We create an instance of our app using our Flask
app.config['REDIS_URL'] = REDIS_URL                     # 2. Save the url for redis in our Flask config
redis_store = FlaskRedis(app)                           # 3. Now we make an object to proxy our Redis commands  (via redis-py
r = Redis()                                         # 4. Also make a client for our redis interface (for non strings)
#############################################################################################################




#################################### HERES WHAT SHE KNOWS HOW TO DO #########################################
@app.route('/')                                                     # People will probably request root directory
def index():                                                        # So here is a routine for when that happens
    x = jsonify(r.hgetall('cb.pull.jjj.python'))
    print "X - Type: {}".format(type(x))
    print "Data: {}".format(x)
    return x
    #return redis_store['pyTest']                       # Get a value from redis, and then return it.
#############################################################################################################

app.run()