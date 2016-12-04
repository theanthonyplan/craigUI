import sys, json                        # import system module
key = sys.argv[1]                       # save the first passed value as the hash key
skey = key+'.string'                    # the key we will use once we stringify

from redis import Redis                 # import redis
r = Redis()                             # create a client

try:                                    # try to do something that is failure-prone
    h = r.hgetall(key)                  # query for the hash object
    s = json.dumps(h)                   # stringify it
    r.set(skey, s)                      # append '.string' to key and save it to redis
    print "STRING SAVED AS: " + skey    # if we made it this far, report our success
    print "STRING LENGTH: {} bytes".format(len(s))         # also how long was that?
except Exception():                     # if anything bad happens
    print "Oh shit it happened again!"  # just play it cool.

