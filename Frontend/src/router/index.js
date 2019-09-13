import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/views/Home/HomePage'
import Playground from '@/views/Game/Playground'
import HeroPage from '@/views/Hero/HeroPage'
import HeroDetail from '@/views/Hero/HeroDetailPage'
import EquipmentPage from '@/views/Equipment/EquipmentPage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', name: 'Home', component: Home },
    { path: '/playground', name: 'Playground', component: Playground },
    { path: '/hero', name: 'HeroPage', component: HeroPage },
    { path: '/hero/:slug', name: 'Hero', component: HeroDetail },
    { path: '/equipment', name: 'EquipmentPage', component: EquipmentPage }
  ]
})
