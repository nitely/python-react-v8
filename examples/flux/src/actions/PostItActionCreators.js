import React, { Component } from 'react'
import PostItAppDispatcher from '../dispatcher/PostItAppDispatcher'
import { CREATE_POST_IT } from '../constants/PostItConstants'
import PostItUtils from '../utils/PostItUtils'
import PostItAPIUtils from '../utils/PostItAPIUtils'


export default {
  createPostIt(text) {
    // Called from composer
    PostItAppDispatcher.dispatch({
      type: CREATE_POST_IT,
      text: text
    })
    PostItAPIUtils.createPostIt(
      PostItUtils.getCreatedPostItData(text))
  },

  fetchAll() {
    // Called from section
    PostItAPIUtils.getAllPostIts()
  }
}
