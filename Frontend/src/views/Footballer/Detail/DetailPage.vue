<template>
  <div class="" v-if="fetched">
    <div class="blurred-background bg-div" :style="{ backgroundImage: 'url(' + footballer.thumbnail + ')' }"></div>
    <div class="container">
      <h1 class="bold is-size-3">{{footballer.name}}</h1>
      <div class="tabs">
        <ul>
          <li class="is-active"><a>English</a></li>
          <li><a>Tiếng Việt</a></li>
          <li><a>Videos</a></li>
          <li><a>Documents</a></li>
        </ul>
      </div>
    </div>

  </div>
</template>

<script>
import API from '@/api'
export default {
  data () {
    return {
      footballer: null,
      fetched: false
    }
  },
  beforeRouteEnter(to, from, next) {
    if (to.params.init_data) {
      next(vm => {
        vm.footballer = to.params.init_data
        vm.fetched = true
      })
    } else {
      API.getFootballerDetail(to.params.id).then(footballer => {
        next(vm => {
          vm.footballer = footballer
          vm.fetched = true
        })
      }).catch(err => {
        next(vm => {
          vm.fetched = true
        })
      })
    }
  }
}
</script>

<style lang="scss">
.blurred-background {
      filter: blur(3px);
      opacity: 0.2;
      height: 100%;
      background-position: center;
      background-repeat: no-repeat;
      background-size: cover;
      z-index: 0;
    }
</style>
