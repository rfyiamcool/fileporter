#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import os,sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.template as template
from tornado.options import define, options
#define("port", default=8888,help="run on the given port", type=int)
define("address", default='0.0.0.0',help="run on the given port", type=int)
logging.basicConfig(level=logging.INFO)

class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/", IndexHandler),
            (r"/upload/([A-Za-z0-9\_\.\-]+)", UploadHandler),
            (r"/undefined", ErrorHandler),
        ]
        
        settings = dict(
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings) 
class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        items = []
        for filename in os.listdir("."):
            items.append(filename)
        self.render('static/index.html', items=items)
    def post(self):
        file_content = self.request.files['file'][0]['body']
        file_name = self.request.files['file'][0]['filename']
        x = open("upload/" + file_name, 'w')
        x.write(file_content)
        x.close()
        self.redirect("/")
class UploadHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self, filename):
        x = open("" + filename)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        self.finish(x.read())
class ErrorHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.redirect('/')
def main():
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), xheaders=True)
    logging.info('Serving HTTP on 0.0.0.0 port %d ...' % port)
    http_server.listen(port,options.address)
    tornado.ioloop.IOLoop.instance().start()
if __name__ == "__main__":
    main()
