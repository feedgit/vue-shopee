<template>
  <div id="app">
    <AppHeader/>
    <main>
      <img src="./assets/logo.png" alt="Vue.js PWA">
      <router-view></router-view>
    </main>
  </div>
</template>

<script>
import AppHeader from '@/components/common/Header'
export default {
  name: 'app',
  components: {
    AppHeader
  }
}
</script>

<style lang="scss">
@import 'assets/bulma.css'
</style>
