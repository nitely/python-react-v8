# -*- coding: utf-8 -*-

from unittest.mock import patch
import unittest
import logging
import collections

import react
from react.react import _DEFINE_GLOBALS_SCRIPT


logging.disable(logging.CRITICAL)


class ReactTest(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_set_up(self):
        """
        It should call utils.setup
        """
        with patch('react.utils.set_up', autospec=True) as s:
            with patch('react.utils.run_script', autospec=True) as r:
                react.set_up()
                s.assert_called_once_with()
                r.assert_called_once_with(_DEFINE_GLOBALS_SCRIPT)

    def test_set_up_globals(self):
        """
        It should register globals
        """
        react.utils.run_script('global.foo = "foo"')
        self.assertEqual(react.utils.run_script('global.foo'), 'foo')
        self.assertEqual(react.utils.run_script('delete global.foo'), 'true')
        self.assertEqual(react.utils.run_script('console.warn()'), 'undefined')
        self.assertEqual(react.utils.run_script('console.error()'), 'undefined')
        self.assertEqual(react.utils.run_script('console.info()'), 'undefined')
        self.assertEqual(react.utils.run_script('console.log()'), 'undefined')

    def test_build_js_script(self):
        """
        It should build the react call
        """
        data = collections.OrderedDict((
            ('foo', 'foo'),
            ('bar', 1)))
        react_ = react.React(data)
        self.assertEqual(
            'global.RenderToString({"foo": "foo", "bar": 1})',
            react_.build_js_script())

    def test_render(self):
        """
        It should call react
        """
        data = collections.OrderedDict((
            ('foo', 'foo'),
            ('bar', 1)))
        react_ = react.React(data)

        with patch('react.utils.run_script', autospec=True) as r:
            r.return_value = 'foo'
            self.assertEqual('foo', react_.render())
            r.assert_called_once_with(
                'global.RenderToString({"foo": "foo", "bar": 1})')

    def test_render_exception(self):
        """
        It should propagate V8 exceptions
        """
        react_ = react.React({})

        with patch(
                'react.utils.run_script',
                autospec=True,
                side_effect=react.excepts.V8Error) as r:
            self.assertRaises(react.excepts.V8Error, react_.render)
            r.assert_called_once_with(
                'global.RenderToString({})')

    def test_to_json(self):
        """
        It should convert data to json
        """
        self.assertEqual(
            '{"foo": "foo", "bar": 1}',
            react.React.to_json(collections.OrderedDict(
                (('foo', 'foo'), ('bar', 1)))))
        self.assertEqual(
            '{"foo": "foo", "bar": 1}',
            react.React.to_json('{"foo": "foo", "bar": 1}'))

    def test_to_dict(self):
        """
        It should convert json to dict
        """
        self.assertDictEqual(
            {"foo": "foo", "bar": 1},
            react.React.to_dict('{"foo": "foo", "bar": 1}'))
