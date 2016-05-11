import { EventEmitter } from 'events'
import PostItAppDispatcher from '../dispatcher/PostItAppDispatcher'
import { CREATE_POST_IT, RECEIVE_RAW_POST_ITS } from '../constants/PostItConstants'
import PostItUtils from '../utils/PostItUtils'


const CHANGE_EVENT = 'change'


let _store = null


function createStore() {
  _store = {
    postIts: {},
    ignoreNextFetch: false
  }
}


function _receiveRawPostItsHelper(rawPostIts) {
  rawPostIts.forEach((rawPostIt) => {
    const postIt = PostItUtils.convertRawPostIt(rawPostIt)
    _store.postIts[postIt.id] = postIt
  })
}


class _PostItStore extends EventEmitter {

  emitChange() {
    this.emit(CHANGE_EVENT)
  }

  addChangeListener(cb) {
    this.on(CHANGE_EVENT, cb)
  }

  removeChangeListener(cb) {
    this.removeListener(CHANGE_EVENT, cb)
  }

  getAll() {
    return _store.postIts
  }

  getList() {
    const postIts = this.getAll()
    return Object.keys(postIts).map(k => postIts[k])
  }

  getListByDate() {
    const postIts = this.getList()

    postIts.sort(function(a, b) {
      if (a.date < b.date) {
        return -1
      } else if (a.date > b.date) {
        return 1
      }
      return 0
    })

    return postIts
  }

  shouldPreLoad() {
    return _store.ignoreNextFetch
  }

  shouldFetch() {
    const ignoreNextFetch = _store.ignoreNextFetch
    _store.ignoreNextFetch = false
    return (!ignoreNextFetch)
  }

  load(data) {
    // Pre-load server side data.
    // You can only call
    // *synchronous* code here.
    // This is called outside
    // the data-flow cycle.
    createStore()
    _receiveRawPostItsHelper(data.rawPostIts)
    _store.ignoreNextFetch = true
  }

}


const PostItStore = new _PostItStore()


PostItAppDispatcher.register((action) => {
  switch (action.type) {

    case CREATE_POST_IT:
      const postIt = PostItUtils.getCreatedPostItData(action.text)
      _store.postIts[postIt.id] = postIt
      PostItStore.emitChange()
      break

    case RECEIVE_RAW_POST_ITS:
      _receiveRawPostItsHelper(action.rawPostIts)
      PostItStore.emitChange()
      break

    // case RECEIVE_RAW_CREATED_POST_ITS
      // You may update the stored postIt
      // with received server side data
      // (ie: the real id)

    default:
      // do nothing
  }
})


export default PostItStore
