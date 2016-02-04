import web
from settings import *

class Default:
    '''
    Default returns a general response
    '''
    def __init__(self):
        pass

    def GET(self):
        web.header("Access-Control-Allow-Origin", "*")
        web.header("Content-Type", "text/html; charset=utf-8")
        web.header("Cache-Control", "no-cache")
        web.header("Pragma", "no-cache")
        web.header("Expires", "0")
        try:
            file = open('%s/%s/%s' % (ROOT_DIR, 'mediasite', 'templates/index.html'), 'r')
            response = file.read()
            return response
        except Exception, inst:
            response = inst
            return response

    def POST(self):
        pass

