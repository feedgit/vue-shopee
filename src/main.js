// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

// Progress bar
import VueInsProgressBar from '@/components/progress-bar'
const options = {
  position: 'fixed',
  show: true,
  height: '3px'
}

Vue.use(VueInsProgressBar, options)
import LazyImage from '@/components/LazyImg'
Vue.component('lazy-img', LazyImage)

// Sweet Alert
import swal from 'sweetalert'
Vue.prototype.$swal = Vue.$swal = swal

// Ready for localforage
import LocalForage from 'localforage'
LocalForage.config({
    driver      : LocalForage.IndexedDB,
    name        : 'LOCALDB',
    version     : 1.0,
    storeName   : 'soccer-localdb'
});
LocalForage.setItem('hero.heroes', {})

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: { App }
})
