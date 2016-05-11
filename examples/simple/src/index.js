import React, { Component } from 'react'
import ReactDOM from 'react-dom'
import ReactDomServer from 'react-dom/server'


class Counter extends Component {
  static defaultProps = {
    initialCount: 0
  }

  state = {
    count: this.props.initialCount
  }

  tick() {
    const { count } = this.state
    this.setState({count: count + 1})
  }

  render() {
    const { count } = this.state
    
    return <div onClick={::this.tick}>
        Clicks: {count}
      </div>
  }
}


if (typeof window !== 'undefined')
  ReactDOM.render(
    <Counter {...window.preLoadedState} />,
    document.querySelector('#content'))
else {
  global.RenderToString = function RenderToString(opts) {
    return ReactDomServer.renderToString(
      React.createElement(opts.component, opts.data))
  }
}
