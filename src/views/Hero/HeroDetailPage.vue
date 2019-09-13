<template>
  <div class="hero-detail-page">
    <div class="container" v-if="hero">
      <div class="columns">
        <div class="column is-one-quarter abilities-col">
          <div class="abilities-row">
            <h2 class="is-size-5">Damage</h2>
            <div class="abilities level">
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Physical Damage</p>
                  <p class="title">{{hero.physical_damage}}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Magical Damage</p>
                  <p class="title" :style="[ hero.magic_damage > 200 ? { color: 'red' } : {} ]">{{hero.magic_damage}}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="abilities-row">
            <h2 class="is-size-5">Defence</h2>
            <div class="abilities level">
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Physical Defence</p>
                  <p class="title">{{hero.physical_defence}}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Magical Defence</p>
                  <p class="title">{{hero.magic_defence}}</p>
                </div>
              </div>
            </div>
          </div>
          <div class="abilities-row">
            <h2 class="is-size-5">Physical</h2>
            <div class="abilities level">
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Attack to heal</p>
                  <p class="title">{{hero.attack_to_heal}}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Health</p>
                  <p class="title">{{hero.health}}</p>
                </div>
              </div>
              <div class="level-item has-text-centered">
                <div>
                  <p class="heading">Mana</p>
                  <p class="title">{{hero.mana}}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="column is-two-quarter">
          <figure class="hero-canvas">
            <img :src="hero.thumbnail" height="375" width="auto" />
            <div class="hero-information">
              <h1 class="bold is-size-3">{{hero.name}}</h1>
            </div>
          </figure>
        </div>
        <div class="column is-one-quarter">
          <div class="right-col-row">
            <h2 class="is-size-5">Price</h2>
            <span class="price is-size-4">{{hero.price === 0 ? 'Free' : hero.price + ' gold'}}</span>
            <a @click="buyHero" class="button buy-button" :class="{ 'owned': hero.request_owned }">{{ hero.request_owned ? 'Owned' : hero.price === 0 ? 'Get free' : 'Buy' }}</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import API from '@/api'
export default {
  data () {
    return {
      hero: null
    }
  },
  beforeRouteEnter(to, from, next) {
    API.getHeroDetail(to.params.slug).then(hero => {
      next(vm => {
        vm.hero = hero
      })
    }).catch(err => {
      next()
    })
  },
  methods: {
    buyHero () {
      API.buyHero()
    }
  }
}
</script>

<style lang="scss">
.hero-detail-page {
  .abilities-col {
    text-align: center;
    .abilities-row {
      background: #080808;
      margin-bottom: 10px;
      .level-item {
        margin-bottom: 5px;
      }
      .title {
        color: #fbd971;
      }
      h2 {
        margin-bottom: 10px;
      }
    }
  }
  .right-col-row {
    display: flex;
    flex-direction: column;
    .price {
      color: #fbd971;
      margin-bottom: 15px;
    }
    .buy-button {
      &.owned {
        color: #73ef16;
        border-color: #73ef16;
      }
    }
  }
  .hero-canvas {
    text-align: center;
    background: #080808;
    padding: 10px;
    .hero-information {
    }
  }
}
</style>
