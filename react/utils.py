# -*- coding: utf-8 -*-

from v8cffi import shortcuts

__all__ = [
    'set_up',
    'load_libs',
    'run_script']


def set_up():
    """
    Setup V8 machinery.\
    Should be called once\
    in the app lifetime,\
    usually through :py:func:`react.set_up()`.
    """
    shortcuts.set_up()


def load_libs(scripts_paths):
    """
    Load JavaScript libs into the\
    global V8 context for later use.

    :param list scripts_paths: List of javascript files
    """
    (shortcuts
     .get_context()
     .load_libs(scripts_paths))


def run_script(script):
    """
    Execute a script (i.e. a function call)\
    into the global V8 context.

    :param str script: Code to execute\
    within the V8 context
    """
    return (shortcuts
            .get_context()
            .run_script(script))
