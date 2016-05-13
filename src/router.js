import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from 'Dashboard'

Vue.use(VueRouter)

const router = new VueRouter({
  history: true,
  linkActiveClass: 'active'
})

router.map({
  '/': {
    name: 'Dashboard',
    component: Dashboard
  }
})

router.redirect({
  '*': '/'
})

export default router
