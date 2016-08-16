# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import json

import six

from . import utils

__all__ = [
    'set_up',
    'React']

_DEFINE_GLOBALS_SCRIPT = (
    'var global = global || this,'
    'console = console || {'
    '  warn: function(){},'
    '  error: function(){},'
    '  log: function(){},'
    '  info: function(){}};')


def set_up():
    """
    Setup V8 machinery and define\
    some basic variables into the\
    global V8 context.\
    Should be called once\
    in the app lifetime.

    :raises react.excepts.V8Error: if there was\
    an error running the JS script. This should\
    usually not be handled
    """
    utils.set_up()

    # Create some globals.
    # v8-cffi does not support
    # python callbacks to log
    # console messages
    utils.run_script(_DEFINE_GLOBALS_SCRIPT)


class React:
    """
    Wrap basic functionality to\
    render react views. The only\
    thing it cares is that there\
    is a global.RenderToString(opts)\
    function defined in the pre-loaded\
    js libs. This render function\
    renders a component, matches a route, etc\
    and returns the rendered view\
    or a json with extra data.

    :param dict opts: Dict of parameters the\
    js render function will receive, it must\
    be serializable with json
    """
    def __init__(self, opts):
        self.opts = opts

    def build_js_script(self):
        """
        :return: The call to the JS render function
        :rtype: str
        """
        return ('global.RenderToString({})'
                .format(self.as_json()))

    def render(self):
        """
        :return: Result of the JS render call
        :rtype: str
        :raises react.excepts.V8Error: if there was\
        an error running the JS script
        """
        return utils.run_script(self.build_js_script())

    def as_json(self):
        """
        Serialize :py:attr:`.opts` into a json.\
        This is used internally and can\
        be overridden to provide a faster\
        json serializer.

        :return: Opts in json format
        :rtype: str
        """
        return self.to_json(self.opts)

    @staticmethod
    def to_json(data):
        """
        Serialize a dict into a json.

        :param data: Dict to convert into JSON
        :type data: dict or str
        :return: Received data in json format
        :rtype: str
        """
        if isinstance(data, six.text_type):
            return data

        data_ = json.dumps(data)

        if isinstance(data_, six.binary_type):
            return data_.decode('utf-8')
        else:
            return data_

    @staticmethod
    def to_dict(json_str):
        """
        De-serialize a json string into a python dict.

        :param str json_str: String to convert into dict
        :return: Received string in dict format
        :rtype: dict
        """
        return json.loads(json_str)
