import React, { Component } from 'react'


class PostItItem extends Component {
  static defaultProps = {
    text: ''
  }

  render() {
    return <div className="post-it-item">
        {this.props.text}
      </div>
  }
}

export default PostItItem
