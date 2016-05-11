import RouterSetUp from './router/client'
import RenderToString from './router/server'


if (typeof window !== 'undefined')
  RouterSetUp()
else
  global.RenderToString = RenderToString
