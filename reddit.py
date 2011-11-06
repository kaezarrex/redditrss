#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

FAVICON_URL = 'http://www.reddit.com/favicon.ico'

class MainHandler(webapp.RequestHandler):

    def get(self):
        return

class FaviconHandler(webapp.RequestHandler):
    def get(self):
        self.redirect(FAVICON_URL, permanent=True)

def main():
    urls = [('/?', MainHandler),
            ('/favicon.ico', FaviconHandler)
            ]

    application = webapp.WSGIApplication(urls, debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

