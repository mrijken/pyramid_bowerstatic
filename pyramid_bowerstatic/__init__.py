# -*- coding: utf-8 -*-
import logging
import inspect
import os

import bowerstatic

log = logging.getLogger(__name__)

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
    return bower


def create_components(name, path, use_relative_path=True):
    if not os.path.isabs(path):#use_relative_path:i
        file = inspect.stack()[1][1]
        dir = os.path.split(file)[0]
        path = os.path.join(dir, path)
    return bower.components(name, path)


def create_local_components(name, component_collection):
    return bower.local_components(name, component_collection)


def include(self, components, path_or_resource):
    include = components.includer(self.environ)
    include(path_or_resource)


def includeme(config):
#    bower_config = bowerstatic_config(config)
    bower_config = bowerstatic_config(config.registry.settings)
    bower.publisher_signature = bower_config.get('publisher_signature')
    config.add_request_method(get_bower, 'bower', property=True, reify=True)
    config.add_request_method(include, 'include')
