import { createRouter, createWebHistory } from 'vue-router'

import homeRoutes from '@home/routes.js'
import starRailRoutes from '@starRail/routes.js'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    ...homeRoutes,
    ...starRailRoutes,
  ]
})

export default router
