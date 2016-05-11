
export default {
  // These are for converting post-its
  // from server and user input into
  // objects the components expect

  convertRawPostIt(rawPostIt) {
    return {
      id: 'store_' + rawPostIt.timestamp,
      text: rawPostIt.text,
      date: new Date(rawPostIt.timestamp)
      // realId: rawPostIt.id
    }
  },

  getCreatedPostItData(text) {
    let timestamp = Date.now()
    return {
      id: 'store_' + timestamp,
      text: text,
      date: new Date(timestamp)
    }
  }
}
