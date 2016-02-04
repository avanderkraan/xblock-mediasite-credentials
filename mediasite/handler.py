import web
import json
from settings import *
import ConfigParser

class Handler:
    '''
    Handles incoming http requests and returns a dictionary with configuration
    data for accessing a mediasite via the API server
    e.g. http://<thisserver>/mediasite/<mediasite_url> where mediasite_url
    is the header in the configuration file
    '''
    def __init__(self):
	filename = MEDIASITE_CONFIG_FILE or '/etc/mediasite.conf'
    	self.mediasite_config = ConfigParser.ConfigParser()
    	self.mediasite_config.read(filename)

    def GET(self, mediasite):
        '''
        Processes a HTTP GET request
        mediasite example: collegerama-vs-accept.tudelft.net
        '''
        web.header("Content-Type", "application/json; charset=utf-8")
        web.header("Cache-Control", "no-cache")
        web.header("Pragma", "no-cache")
        web.header("Expires", "0")
        response = None
        try:
            refuse = True
            referer = web.ctx.env.get('REMOTE_ADDR', '')
            #print mediasite, referer
            #print web.ctx.env
    	    username = self.mediasite_config.get(mediasite, 'username')
    	    password = self.mediasite_config.get(mediasite, 'password')
    	    apikey = self.mediasite_config.get(mediasite, 'apikey')
    	    token_life_time = int(self.mediasite_config.get(mediasite,
                                                           'token_life_time'))
            origin_whitelist = list(self.mediasite_config.get(mediasite,
                'origin_whitelist').split(','))
            checked_referer = False
            for item in origin_whitelist:
                item = item.strip()
                if referer.startswith(item, 0, len(item)):
                    refuse = False
                    web.header("Access-Control-Allow-Origin", referer)
                    checked_referer = True
                    break
            if checked_referer and refuse:
                web.header("Access-Control-Allow-Origin", "*")

            if refuse == True:
                response = {'error': 'Origin %s is not allowed to access %s' % (referer, web.ctx.env.get('SERVER_NAME', ''))}
            	return json.dumps(response)
 
            result = {} 
            result['username'] = username
            result['password'] = password
            result['apikey'] = apikey
            result['token_life_time'] = token_life_time

            response = {'data': result}
            return json.dumps(response)

        except Exception, inst:
            pass
            response = {'error': '%s' % inst}
        return json.dumps(response)

    def POST(self):
        '''
        Processes a HTTP POST request
        '''
        pass

