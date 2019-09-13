<template>
  <div class="hero-card">
    <router-link :to="{ name: 'Hero', params: { id: hero.id, slug: hero.slug, init_data: hero } }" class="bg-div player-card-container">
      <div class="playercard-picture">
        <lazy-img class="" :src="hero.thumbnail" />
      </div>
    </router-link>
    <div class="tag-bottom">
      <div class="player-name">{{hero.name}}</div>
      <a class="button is-small buy-button" :class="{ 'owned': hero.request_owned }">{{ hero.request_owned ? 'Owned' : hero.price === 0 ? 'Free' : hero.price + ' gold' }}</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    hero: Object
  }
}
</script>

<style lang="scss">
.hero-card {
  overflow: hidden;
  display: block;
  border-radius: 10px;
  position: relative;
  padding-top: 150%;
  .player-card-container {
    background-size: 100% 100%;
    background-image: url('/static/img/texture-card.jpg');
    .playercard-picture {
      position: absolute;
      top: 10%;
      left: 15%;
      right: 15%;
      bottom: 30%;
      background: radial-gradient(#f1ca54, #ecc54d, #ffc000);
      border-radius: 10px;
      text-align: center;
      img {
        transform: scale(1.25);
        max-width: 100%;
        max-height: 100%;
        margin-top: -10px;
      }
    }
  }
  .tag-bottom {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 0;
    text-align: center;
    padding: 15px 10px 10px 10px;
    .player-name {
      text-align: center;
      font-weight: 700;
      font-size: 85%;
      color: #e9cc74;
      text-transform: uppercase;
      white-space: nowrap;
      overflow: hidden;
      z-index: 4;
    }
    .buy-button {
      margin-top: 5px;
      background: none;
      color: #FFF;
      &.owned {
        color: #73ef16;
        border-color: #73ef16;
      }
    }
  }
}
</style>
