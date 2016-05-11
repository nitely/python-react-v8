import PostItServerActionCreators from '../actions/PostItServerActionCreators'


// !!! Please Note !!!
// In a real-world scenario, this
// would involve XMLHttpRequest, or perhaps a newer client-server protocol.
// The function signatures below might be similar to what you would build, but
// the contents of the functions are just trying to simulate client-server
// communication and server-side processing.

// todo: pre-populate with server data
var postIts = []


export default {
  getAllPostIts() {
    // Simulate API call success
    setTimeout(() => {
      PostItServerActionCreators.receiveAll(postIts)
    }, 0)
  },

  createPostIt(data) {
    // Simulate API call success
    let timestamp = Date.now()
    const createdPostIt = {
      id: '' + timestamp,
      text: data.text,
      timestamp: timestamp
    }
    postIts.push(createdPostIt)
    setTimeout(() => {
      PostItServerActionCreators.receiveCreatedPostIt(createdPostIt)
    }, 0)
  }
}
