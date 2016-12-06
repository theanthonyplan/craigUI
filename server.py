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
import redis                                 #  Get regular Redis interface too, just in case for hashes
#############################################################################################################



#################################### OK FAM, LETS GET TO WORK ###############################################
app = Flask(__name__)                                   # 1. We create an instance of our app using our Flask
app.config['REDIS_URL'] = REDIS_URL                     # 2. Save the url for redis in our Flask config
#redis_store = FlaskRedis(app)                           # 3. Now we make an object to proxy our Redis commands  (via redis-py
r = redis.StrictRedis(host='localhost', port=6379, db=0)                                         # 4. Also make a client for our redis interface (for non strings)
#############################################################################################################




#################################### HERES WHAT SHE KNOWS HOW TO DO #########################################
@app.route('/<obj_type>/<query>')                                                     # obj_type is etiher s for string or h for h, query is the key to use
def index(obj_type, query):
    x = 'blank'
    print 'OBJ_TYPE: ' + obj_type 
    print 'QUERY: ' + query                                                        # So here is a routine for when that happens
    if obj_type == 'h':
        x = jsonify(r.hgetall(query))
    else:
        x = jsonify(r.get(query))
    print "X - Type: {}".format(type(x))
    print "X - Data: {}".format(x)
    return x
    #return redis_store['pyTest']                       # Get a value from redis, and then return it.
#############################################################################################################

app.run(host='0.0.0.0', port='5200')
