import os
import sys
import web

path = '%s/%s' % ('/var/www/wsgi', 'mediasite')
if path not in sys.path:
    sys.path.append(path)

from handler import Handler
from default import Default

urls = (
     '/(.*)/', 'Handler',
     '.*', 'Default',
)
application = web.application(urls, globals()).wsgifunc()

