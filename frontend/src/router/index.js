import Vue from 'vue'
import Router from 'vue-router'
import Index from '@/index/Index'
import Hello from '@/components/HelloWorld'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index
    },
    {
      path: '/hello',
      name: 'Index',
      component: Hello
    }
  ]
})
