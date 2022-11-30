from tornado.web import RequestHandler, Application
import tornado
import json
from pika_client import PikaClient


class MainHandler(RequestHandler):

    @property
    def pika(self):
        return self.application.pika

    @tornado.gen.coroutine
    def post(self):
        print('requests starts...')
        data = self.get_argument('firstname', None)
        data = {
            'firstname': self.get_argument('firstname', None),
            'lastname': self.get_argument('lastname', None),
            'dad': self.get_argument('dad', None),
            'phone': self.get_argument('phone', None),
            'text': self.get_argument('text', None)
        }
        self.pika.send_message(json.dumps(data))

def make_app():
    return Application([
        (r"/", MainHandler),
    ],)

def main():
    app = make_app()
    io_loop = tornado.ioloop.IOLoop.instance()
    app.pika = PikaClient()
    app.pika.connect()
    app.pika.create_queue()
    app.listen(8888)
    io_loop.start()

if __name__ == "__main__":
    main()