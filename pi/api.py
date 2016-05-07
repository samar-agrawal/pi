import os

from flask import Flask, redirect, request
from namutil import get_graylogger, RedisClient
import base64
import md5

app = Flask(__name__, instance_relative_config=True)

REDIS_SERVER = {
    'host': app.config['REDIS_HOST'],
    'port': app.config['REDIS_PORT']
     }

rc = RedisClient(**REDIS_SERVER)

def md5key(url):
    return base64.b64encode(md5.new(url).digest()[-4:]).replace('=','').replace('/','_')

@app.route('/', methods=['POST'])
def shorten():
    payload = request.get_json()
    logger.info("URL shortener triggered", extra={'payload':payload})
    url = payload['url']
    code = md5key(url)
    logger.info("URL %s: %s"%(url, code))
    rc.hset(app.config['REDIS_KEY'], code, url) 
    return {'shorturl':url_host+code, 'url':url, 'code':code}

@app.route('/<code>')
def lookup(code):
    idc = rc.hget(app.config['REDIS_KEY'], code)
    return redirect(request.HOST+idc)     

@app.route('/healthcheck')
def healthcheck():
    return ''

@app.after_request
def log_request(response):
    '''Logging method calls '''

    logger.info("[%s] %s %s" % (response.status_code, request.method, request.url))
    return response

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5208)
