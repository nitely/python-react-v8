import React from 'react'
import ReactDOM from 'react-dom'
import { match, RouterContext, Router, browserHistory } from 'react-router'
import { loadData } from './utils'
import routes from './routes'


export default function RouterSetUp() {
  const history = browserHistory

  match({history, routes}, (error, redirectLocation, renderProps) => {
    loadData(renderProps, window.preLoadedState)
    ReactDOM.render(
      <Router {...renderProps} />,
      document.querySelector('#content'))
  })
}
