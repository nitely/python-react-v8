# React-Flux app

In this example every *store* reflects the *state* of
the app given a URL, this way is easy to render server-side,
plus it's the recommended way.

> **Note:** All changes are lost when refreshing the page, there is no persistence.


## Build

```
$ npm install  # requires Node.js to be installed on the system
$ npm run bundle  # builds ./src/bundle.js

$ pip install python-react-v8
$ python build.py  # creates ./index.html

$ npm run start_static  # start dev server and serve ./index.html
```

Open `http://localhost:3000/` in a web-browser.


# Resources

* [Flux](https://facebook.github.io/flux/)
* [Flux: Actions and the Dispatcher](http://facebook.github.io/react/blog/2014/07/30/flux-actions-and-the-dispatcher.html)
* [ServerRendering (react-router 2.4)](https://github.com/reactjs/react-router/blob/v2.4.0/docs/guides/ServerRendering.md)
