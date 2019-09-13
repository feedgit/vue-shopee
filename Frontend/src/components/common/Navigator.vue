<template>
  <div class="container">
    <div class="navigator tabs is-centered">
      <ul>
        <li class="" v-for="(nav, i) in navigators" :key="i">
          <router-link :to="{ name: nav.route }" class="tab">
            <img :src="nav.icon" width="20" />
            <a>{{nav.label}}</a>
          </router-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      navigators: [
        { label: 'Home', icon: '/static/icons/home.svg', route: 'Home' },
        { label: 'Hero', icon: '/static/icons/hero.svg', route: 'HeroPage' },
        { label: 'Equipment', icon: '/static/icons/sword.svg', route: 'EquipmentPage' },
        { label: 'Battleground', icon: '/static/icons/battle.svg', route: 'Playground' },
      ]
    }
  }
}
</script>

<style lang="scss">
.navigator.tabs {
  .tab {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    &.router-link-exact-active {
      text-shadow: 0px 0px 22px white;
    }
  }
}
</style>
