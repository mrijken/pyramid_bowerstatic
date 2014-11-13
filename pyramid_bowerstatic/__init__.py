# -*- coding: utf-8 -*-
import inspect
import os
import inspect

import bowerstatic

bower = bowerstatic.Bower()


def bowerstatic_config(settings, prefix='bowerstatic.'):
    cfg = {
        'publisher_signature': 'bowerstatic',
    }
    for k, v in settings.items():
        if k.startswith(prefix):
            cfg[k[len(prefix):]] = v
    return cfg


def get_bower():
    """returns the active Bower instance"""
    return bower


def create_components(name, path):
    """Convinience function for bower.components
    """
    return bower.components(name, path)


def create_local_components(name, component_collection):
    """Convinience function for bower.local_components
    """
    return bower.local_components(name, component_collection)


class tween_factory(object):
    def __init__(self, handler, registry):
        self.handler = handler
        self.registry = registry

    def __call__(self, request):
        response = self.handler(request)

        injector = bower.injector(wsgi=None)
        publisher = bower.publisher(wsgi=None)

        response = publisher.publish(request, injector.inject(request, response))

        return response


def include(self, components, path_or_resource):
    """
    Mark the given `path_or_resource` of the given `components`.
    When this is done, the corresponding resources (including resources on which these depends)
    will be inserted in the header of the html response.
    """
    include = components.includer(self.environ)
    include(path_or_resource)


def get_bowerstatic_path(self, components_name, component_name, resource_name):
    """
    Returns the url of the bower resources, so it can be used manualy in a view.
    """
    components =  bower._component_collections[components_name]
    return components.get_component(component_name).url() + resource_name


def includeme(config):
    bower_config = bowerstatic_config(config.registry.settings)
    bower.publisher_signature = bower_config.get('publisher_signature')

    config.add_tween('pyramid_bowerstatic.tween_factory')
    config.add_request_method(lambda:bower, 'bower', property=True, reify=True)
    config.add_request_method(include, 'include')
    config.add_request_method(get_bowerstatic_path, 'get_bowerstatic_path')
