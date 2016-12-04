from flask import Flask                                                 # import flask
from lark.ext.flask.redis_api import redis_api_blueprint                # get the blueprint for our rest api
from lark.ext.flask.flask_redis import Redis                            # get the interface for flask

app = Flask(__name__)                                                   # create a flask app, passing it the name of this file
Redis(app)                                                              # Add a simple redis connection to the global object

app.config['DEFAULT_LARK_SCOPES'] = set(['admin'])                      # Save config to flask
app.register_blueprint(redis_api_blueprint, url_prefix='/api/0')        # Mount the redis blueprint

if __name__ == '__main__':                                              # Dont run this stuff if someone imports this file
    app.run()                                                           # Only run it if it is the executing file