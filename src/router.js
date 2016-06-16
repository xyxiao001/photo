import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from 'Dashboard'
import Photo from 'Photo'
import Video from 'Video'
import Biao from 'Biao'
import Icon from 'Icon'
import Login from 'Login'

Vue.use(VueRouter)

const router = new VueRouter({
  history: true,
  linkActiveClass: 'active'
})

router.map({
  '/': {
    name: 'Dashboard',
    component: Dashboard
  },
  '/login': {
    name: 'Login',
    component: Login
  },
  '/photo': {
    name: 'Photo',
    component: Photo
  },
  '/biao': {
    name: 'Biao',
    component: Biao
  },
  '/video': {
    name: 'Video',
    component: Video
  },
  '/icon': {
    name: 'Icon',
    component: Icon
  }
})

router.redirect({
  '*': '/'
})

export default router
