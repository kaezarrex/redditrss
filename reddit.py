#!/usr/bin/env python

from google.appengine.ext import webapp
from google.appengine.ext.webapp import util

class MainHandler(webapp.RequestHandler):

    def get(self):
        return

def main():
    urls = [('/?', MainHandler),
            ]

    application = webapp.WSGIApplication(urls, debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()

