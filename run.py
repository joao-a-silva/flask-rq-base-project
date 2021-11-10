import os

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop

from app import app

if __name__ == "__main__":

    if os.getenv('FLASK_CONFIG') == 'development':
        app.run(host = '0.0.0.0' , port = 5000)
    else:

        http_server = HTTPServer(WSGIContainer(app))
        http_server.listen(5000)
        IOLoop.instance().start()
