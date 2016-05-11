import React, { Component } from 'react'
import PostItComposer from './PostItComposer'
import PostItItem from './PostItItem'
import PostItStore from '../stores/PostItStore'
import PostItActionCreators from '../actions/PostItActionCreators'


class PostItSection extends Component {
  state = {
    postIts: []
  }

  constructor(props) {
    super(props)
    this._onChange = this._onChange.bind(this)

    if (PostItStore.shouldPreLoad())
      this.state.postIts = PostItStore.getListByDate()
  }

  render() {
    const PostItItems = this.state.postIts.map((postIt) => {
      return <PostItItem {...postIt} key={postIt.id} />
    })

    return <div className="post-it-section">
        <PostItComposer />
        {PostItItems}
      </div>
  }

  componentDidMount() {
    PostItStore.addChangeListener(this._onChange)

    if (PostItStore.shouldFetch())
      PostItActionCreators.fetchAll()
  }

  componentWillUnmount() {
    PostItStore.removeChangeListener(this._onChange)
  }

  _onChange() {
    this.setState({postIts: PostItStore.getListByDate()})
  }

  static getStore() {
    return PostItStore
  }
}

export default PostItSection
