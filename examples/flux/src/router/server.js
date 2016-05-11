import React from 'react'
import ReactDomServer from 'react-dom/server'
import { match, RouterContext, Router } from 'react-router'
import { loadData } from './utils'
import routes from './routes'


export default function RenderToString(opts) {
  const res = {
    status: 200,
    error: '',
    redirection: '',
    result: ''
  }

  match({routes, location: opts.url}, (error, redirectLocation, renderProps) => {
    if (error) {
      res.status = 500
      res.error = error.message
    } else if (redirectLocation) {
      res.status = 302
      res.redirection = redirectLocation.pathname + redirectLocation.search
    } else if (renderProps) {
      loadData(renderProps, opts.data)
      res.result = ReactDomServer.renderToString(<RouterContext {...renderProps} />)
    } else {
      res.status = 404
      res.error = 'Not found'
    }
  })

  return JSON.stringify(res)
}
