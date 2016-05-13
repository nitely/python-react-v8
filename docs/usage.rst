.. _usage:

Usage
=====

Quick-start
-----------

::

    import react

    react.set_up()
    react.utils.load_libs(['./bundle.js'])
    react_ = react.React({
        'component': 'Counter',
        'data': {'InitialCount': 10}})
    react_.render()
    # <div>Count: 10</div>

First, we must call `set_up()`, this will initialize the V8 machinery.
It must be call once in the program lifetime so it's a good idea to call
it at import time or before starting the web-server.

Then, we load the js bundle, it should be the same that is provided to the browser.

Then, we create the `React` object, passing the parameters the underlying
JS renderer function will receive. It must contain serializable (as json)
keys and variables.

Finally, we call the `render()` method, to run the JS renderer function and
get its return value, which usually is a serializable object containing the
rendered component and other extra data like an error message, redirection, etc.

Fake web-framework
------------------

::

    import react

    from my_web_framework import render, orm, runserver


    def index(request):
        """A naive implementation for a fake web-framework"""
        data = orm.query().only('name', 'age', 'location')
        react_ = react.React({
            'url': request.get_full_url(),
            'data': data})
        context = {
            'content': react_.render(),
            'data': react_.to_json(data)}

        return render('index.html', context)


    if __name__ == '__main__':
        react.set_up() # Initialize V8 machinery
        react.utils.load_libs(['./bundle.js'])
        runserver(index)

This is pretty much the same as the "quick start" example.

But there are two things to have in mind:

    1. Always make the query including the fields that the react view requires,
       don't fetch everything, doing so may end up leaking information since
       it gets exposed as a JS object within the HTML.
    2. The data passed to react should be exactly the same as the data provided
       by the API endpoint for that view, so the query should be the same.


Multiple stores
---------------

::

    # ...
    data = {
        'postIts': orm.query().all().only('id', 'text'),
        'comments': orm.query().all().only('id', 'created_by', 'comment_html')
    }
    # ...

Seriously.


Handling errors
---------------

::

    import react

    # ...
    try:
        content = react_.render()
    except react.excepts.V8Error as err:
        logger.error(err)
        content = ''
    # ...

When handling exceptions, there is not much to do other
than set an empty content and let react render it client-side.

The data can still be pre-loaded, assuming the error wasn't
thrown by the load function.

It may be a good idea to log the data (as json) to replicate
the error later. Since most of the logic is the same client-side,
once you have replicated it, it can be debugged in the web-browser.
