import os
import pyramid
import pyramid_bowerstatic
import bowerstatic
from webtest import TestApp as Client
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def test_static():
    def view(request):
        request.include(components, 'jquery')
        return Response('<html><head></head><body></body></html>')

    components = pyramid_bowerstatic.create_components(
        'myapp', os.path.join(os.path.dirname(__file__), 'bower_components'))

    config = Configurator()
    config.add_route('view', '/')
    config.add_view(view, route_name='view')
    config.include('pyramid_bowerstatic')
    app = config.make_wsgi_app()

#    c = Client(pyramid_bowerstatic.bower.wrap(app))
    c = Client(app)
    response = c.get('/')

    assert response.body == (
        b'<html><head>'
        b'<script type="text/javascript" '
        b'src="/bowerstatic/myapp/jquery/2.1.1/dist/jquery.js"></script>'
        b'</head><body></body></html>')

    response = c.get("/bowerstatic/myapp/jquery/2.1.1/dist/jquery.js")

    assert response.body == '/* this is a fake jquery.js */\n'
