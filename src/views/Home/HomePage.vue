<template>
  <div class="container homepage">
    
  </div>
</template>

<script>
import API from '@/api'
import FootballerCard from '@/views/Footballer/FootballerCard'
import HeroHouse from '@/views/Hero/HeroHouse'
export default {
  data () {
    return {
    }
  },
  methods: {
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
