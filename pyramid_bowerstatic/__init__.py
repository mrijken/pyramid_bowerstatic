# -*- coding: utf-8 -*-
import inspect
import os

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
    if not os.path.isabs(path):
        file = inspect.stack()[1][1]
        dir = os.path.split(file)[0]
        path = os.path.join(dir, path)
    return bower.components(name, path)


def create_local_components(name, component_collection):
    """Convinience function for bower.local_components
    """
    return bower.local_components(name, component_collection)


def include(self, components, path_or_resource):
    """
    Mark the given `path_or_resource` of the given `components`.
    When this is done, the corresponding resources (including resources on which these depends)
    will be inserted in the header of the html response.
    """
    include = components.includer(self.environ)
    include(path_or_resource)


def includeme(config):
    bower_config = bowerstatic_config(config.registry.settings)
    bower.publisher_signature = bower_config.get('publisher_signature')
    config.add_request_method(lambda:bower, 'bower', property=True, reify=True)
    config.add_request_method(include, 'include')
