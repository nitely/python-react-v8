import PostItAppDispatcher from '../dispatcher/PostItAppDispatcher'
import { 
  RECEIVE_RAW_POST_ITS,
  RECEIVE_RAW_CREATED_POST_ITS } from '../constants/PostItConstants'


export default {

  receiveAll(rawPostIts) {
    PostItAppDispatcher.dispatch({
      type: RECEIVE_RAW_POST_ITS,
      rawPostIts: rawPostIts
    })
  },

  receiveCreatedPostIt(createdPostIt) {
    PostItAppDispatcher.dispatch({
      type: RECEIVE_RAW_CREATED_POST_ITS,
      rawPostIts: createdPostIt
    })
  }

}
