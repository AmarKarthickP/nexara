import { createRouter, createWebHistory } from 'vue-router'

import Nexara from '@/views/Nexara.vue'
import TestView from '@/views/TestView.vue'
import HomePage from '@/pages/HomePage.vue'

const routes = [
  {
    path: '/test',
    name: 'test',
    component: TestView,
  },
  {
    path: '/',
    component: Nexara,
    children: [
      {
        path: '',
        redirect: 'chat'
      },
      {
        path: 'chat',
        name: 'chat',
        component: HomePage
      },
    ]
  }
]

const router = createRouter({
  history: createWebHistory('/nexara/'),
  routes,
})

export default router
