// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Buefy from 'buefy'
import 'buefy/lib/buefy.css'

import App from './App.vue'
import router from './router'
import VueResource from 'vue-resource'

Vue.use(Buefy, {
  defaultIconPack: 'fa'
})

Vue.use(VueResource)

Vue.http.options.root = 'localhost/'

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
