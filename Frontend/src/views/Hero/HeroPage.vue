<template>
  <div class="hero-page container">
    <div class="tabs is-centered">
      <ul>
        <li class="is-active"><a>My heroes</a></li>
        <li><a>Hero Store</a></li>
      </ul>
    </div>
    <div class="tab-content">
      <div class="gridded-heroes">
        <HeroCard v-for="hero in heroes_in_store" :key="hero.id" :hero="hero"/>
      </div>
    </div>
  </div>
</template>

<script>
import API from '@/api'
import HeroCard from '@/components/HeroCard'
export default {
  data () {
    return {
      my_heroes: [],
      heroes_in_store: []
    }
  },
  created () {
    this.fetchHeroes()
  },
  methods: {
    fetchHeroes () {
      API.getHeroList({}).then(res => {
        this.heroes_in_store = res.data
      }).catch(err => {})
    }
  },
  components: {
    HeroCard
  }
}
</script>

<style lang="scss">
.hero-page {
  .tabs {
    li.is-active {
      border-bottom: 1px solid #FFF;
    }
  }
  .tab-content {
    .gridded-heroes {
      display: grid;
      grid-template-columns: repeat(8, 1fr);
      grid-gap: 10px;
    }
  }
}
</style>
