import Vue from 'vue'
import Router from 'vue-router'

Vue.use(Router)

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('./views/Hot.vue')
    },
    {
      path: '/ask',
      name: 'ask',
      component: () => import('./views/Ask.vue')
    },
    {
      path: '/show',
      name: 'show',
      component: () => import('./views/Show.vue')
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('./views/Login.vue')
    }
  ]
})
