

export function loadData(renderProps, data) {
  renderProps.components.forEach((component) => {
    if (typeof component.getStore === 'function')
      component.getStore().load(data)
  })
}
