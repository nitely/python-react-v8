# -*- coding: utf-8 -*-

import os
import time

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
    data = {
        'rawPostIts': [{
            'id': 'id_1',
            'text': 'aloha',
            'timestamp': int(time.time())}]}
    react = React({
        'url': '/',
        'data': data})
    response = react.to_dict(react.render())

    assert response['status'] == 200

    with open(OUTPUT_PATH, 'w', encoding='utf-8') as fh:
        fh.write(template.format(
            pre_rendered_content=response['result'],
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
