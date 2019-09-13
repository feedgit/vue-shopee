<template>
  <div class="equipment-card">
    <router-link :to="{ name: 'Equipment', params: { id: equipment.id, slug: equipment.slug, init_data: equipment } }" class="bg-div player-card-container">
      <div class="playercard-picture">
        <lazy-img class="" :src="equipment.thumbnail" />
      </div>
    </router-link>
    <div class="tag-bottom">
      <div class="player-name">{{equipment.name}}</div>
      <a class="button is-small buy-button">{{ equipment.price === 0 ? 'Free' : equipment.price + ' gold' }}</a>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    equipment: Object
  }
}
</script>

<style lang="scss">
.equipment-card {
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
    }
  }
}
</style>
