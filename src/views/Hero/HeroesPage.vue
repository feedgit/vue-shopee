<template>
  <div class="container homepage">
    <HeroHouse/>
    <div class="tabs">
      <ul>
        <li :class="{ 'is-active' : active_type_id === 2 }" @click="changeType(2)"><a>Footballers</a></li>
        <li :class="{ 'is-active' : active_type_id === 1 }" @click="changeType(1)"><a>Fictional Superheroes</a></li>
        <li :class="{ 'is-active' : active_type_id === 3 }" @click="changeType(3)"><a>Singer / Actress</a></li>
        <li :class="{ 'is-active' : active_type_id === 4 }" @click="changeType(4)"><a>Documents</a></li>
      </ul>
    </div>
    <div class="footballers-widget" v-if="!prefetching">
      <FootballerCard v-for="footballer in human" :key="footballer.id" :footballer="footballer"/>
    </div>
    <span v-else>
      <img src="/static/img/logo.svg" width="30" />
    </span>
  </div>
</template>

<script>
import API from '@/api'
import FootballerCard from '@/views/Footballer/FootballerCard'
import HeroHouse from '@/views/Hero/HeroHouse'
export default {
  data () {
    return {
      active_type_id: 2,
      prefetching: false,
      human: []
    }
  },
  beforeRouteEnter (to, from, next) {
    var init_active_type_id = 2
    API.getHumanList({ type_id: init_active_type_id }).then(res => {
      next(vm => {
        vm.human = res.data
        vm.prefetching = false
      })
    }).catch(err => {
      next(vm => { vm.prefetching = false })
    })
  },
  methods: {
    changeType(type_id) {
      if (type_id === this.active_type_id) { return }
      this.human = []
      this.prefetching = true
      setTimeout(() => {
        this.active_type_id = type_id
        API.getHumanList({ type_id: type_id }).then(res => { this.human = res.data; this.prefetching = false }).catch(err => { this.prefetching = false })
      }, 1000)

    }
  },
  components: {
    HeroHouse,
    FootballerCard
  }
}
</script>

<style lang="scss">
.homepage {
  .footballers-widget {
    margin-top: 10px;
    display: grid;
    grid-template-columns: repeat(8, 1fr);
    grid-gap: 10px;
  }
}
</style>
