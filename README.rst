pyramid_bowerstatic: BowerStatic integration for Pyramid
========================================================

pyramid_bowerstatic integrates BowerStatic_ into Pyramid_.

When create a pyramid app, make sure to include pyramid_bowerstatic and wrap the
wgsi_app with bowerstatic:

    ...
    
    config.include('pyramid_bowerstatic')
    
    ...
    
    app = pyramid_bowerstatic.bower.wrap(config.make_wsgi_app())

Resources can be added to the bowerstatic repository by:

    components = pyramid_bowerstatic.create_components('myapp', os.path.join(os.path.dirname(__file__), 'bower_components'))

And resources can be used in views by:

    request.include(components, 'jquery')


Resource can also be inserted in the view/template directly by using:

   request.get_bowerstatic_url('myapp', 'jquery', 'jquery.js')


.. _BowerStatic: http://bowerstatic.readthedocs.org

.. _Pyramidh: http://docs.pylonsproject.org/projects/pyramid

