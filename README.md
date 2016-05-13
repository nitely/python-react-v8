# Python-React-V8

[![Build Status](https://img.shields.io/travis/nitely/python-react-v8.svg?style=flat-square)](https://travis-ci.org/nitely/python-react-v8)
[![Coverage Status](https://img.shields.io/coveralls/nitely/python-react-v8.svg?style=flat-square)](https://coveralls.io/r/nitely/python-react-v8)
[![pypi](https://img.shields.io/pypi/v/python-react-v8.svg?style=flat-square)](https://pypi.python.org/pypi/python-react-v8)
[![licence](https://img.shields.io/pypi/l/python-react-v8.svg?style=flat-square)](https://raw.githubusercontent.com/nitely/python-react-v8/master/LICENSE)

Thin wrapper around [v8-cffi](https://github.com/nitely/v8-cffi) to render React views server-side.


## Compatibility

[What v8-cffi supports](https://github.com/nitely/v8-cffi#compatibility)


## Install

```
$ pip install python-react-v8
```


## Usage

```python
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
```

Read the [docs](http://python-react-v8.readthedocs.org/en/latest/).


## Examples

* [Flux](https://github.com/nitely/python-react-v8/tree/master/examples/flux)
* [Simple](https://github.com/nitely/python-react-v8/tree/master/examples/simple)


## Build examples

```
$ make build-examples
```


## Tests

```
$ make test
```


## License

MIT
