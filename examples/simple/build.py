# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import os
import io

from react import React
from react import utils


BASE_PATH = os.path.dirname(os.path.abspath(__file__))
OUTPUT_PATH = os.path.join(BASE_PATH, 'index.html')
BUNDLE_PATH = os.path.join(BASE_PATH, 'src', 'bundle.js')


template = """<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Example</title>
    <link rel="stylesheet" href="src/style.css">
  </head>
  <body>
    <div id="content">{pre_rendered_content}</div>
    <script>
      window.preLoadedState = {pre_loaded_state};
    </script>
    <script src="src/bundle.js"></script>
  </body>
</html>
"""


def write_index():
    data = {'initialCount': 10}
    react = React({
        'component': 'Counter',
        'data': data})

    with io.open(OUTPUT_PATH, 'w', encoding='utf-8') as fh:
        fh.write(template.format(
            pre_rendered_content=react.render(),
            pre_loaded_state=react.to_json(data)))


def load_libs():
    utils.load_libs([BUNDLE_PATH])


def do_build():
    load_libs()
    write_index()


if __name__ == '__main__':
    import react
    react.set_up()

    do_build()
