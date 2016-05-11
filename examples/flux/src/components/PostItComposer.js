import React, { Component } from 'react'
import PostItActionCreators from '../actions/PostItActionCreators'


const ENTER_KEY_CODE = 13


class PostItComposer extends Component {
  state = {
    text: ''
  }

  render() {
    return <textarea
        className="post-it-composer"
        name="post-it"
        value={this.state.text}
        onChange={::this._onChange}
        onKeyDown={::this._onKeyDown}
      />
  }

  _onChange(event) {
    this.setState({text: event.target.value})
  }

  _onKeyDown(event) {
    if (event.keyCode === ENTER_KEY_CODE) {
      event.preventDefault()
      const text = this.state.text.trim()

      if (text)
        PostItActionCreators.createPostIt(text)

      this.setState({text: ''})
    }
  }
}

export default PostItComposer
