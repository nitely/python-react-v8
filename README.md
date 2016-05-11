# Python-React-V8

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

* [Flux](https://github.com/nitely/python-react-v8/tree/master/example/flux)
* [Simple](https://github.com/nitely/python-react-v8/tree/master/example/simple)


## License

MIT
