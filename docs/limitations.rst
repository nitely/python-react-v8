.. _contexts:

Limitations
===========

Context
-------

There is just one context. There is no sandboxing.
This means all requests to the server will share
the same JS context.

Creating a new JS context and loading the libs into
it for every request is quite slow.

A solution is to provide a way to create or reset
the stores before doing anything.

Node.js suffers from the same issues.


Event Loop
----------

There is no event loop. This means it is not
possible to run asynchronous operations.

Most (all?) async functions are not available.
For example, calling `setTimeout` will throw a ReferenceError.

This is usually not a problem since it's
something you don't want to do. Rendering
react components to string (server-side)
is synchronous. Any async operation should
take place before calling react, therefore,
it can be done in python code.

Here is a react_issue_ discussing this.

.. _react_issue: https://github.com/facebook/react/issues/1739
