import Vue from 'vue'
import Router from 'vue-router'
import Hello from '@/components/HelloWorld'
import Main from '@/main/Main'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Main',
      component: Main
    },
    {
      path: '/hello',
      name: 'Hello',
      component: Hello
    }
  ]
})
