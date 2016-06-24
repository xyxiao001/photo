import Vue from 'vue'
import VueRouter from 'vue-router'

import Dashboard from 'Dashboard'
import Photo from 'Photo'
import Video from 'Video'
import Biao from 'Biao'
import Icon from 'Icon'
import Login from 'Login'
import PhotoDetail from 'PhotoDetail'
import BiaoDetail from 'BiaoDetail'
import Register from 'Register'
import Search from 'SearchDetail'

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
  '/photo/:id': {
    name: 'PhotoDetail',
    component: PhotoDetail
  },
  '/biao': {
    name: 'Biao',
    component: Biao
  },
  '/biao/:id': {
    name: 'BiaoDetail',
    component: BiaoDetail
  },
  '/video': {
    name: 'Video',
    component: Video
  },
  '/icon': {
    name: 'Icon',
    component: Icon
  },
  '/register': {
    name: 'Register',
    component: Register
  },
  '/search': {
    name: 'Search',
    component: Search
  }
})

router.redirect({
  '*': '/'
})

export default router
