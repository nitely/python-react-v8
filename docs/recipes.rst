.. _recipes:

Recipes
=======

Simple React
------------

::

    from react import React

    from my_web_framework import excepts


    class SimpleReact(React):

        @property
        def data(self):
            return self.to_json(self.opts['data'])

        def render(self):
            res = self.to_dict(
                super().render())
            status = res['status']

            if status == 500:
                raise excepts.HTTPError(res['error'])

            if status == 302:
                raise excepts.HTTPRedirect(res['redirection'])

            if status == 404:
                raise excepts.HTTPNotFound

            return res['result']
