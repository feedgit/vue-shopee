<template>
  <div class="equipment-page container">
    <div class="tabs is-centered">
      <ul>
        <li class="is-active"><a>My equipment</a></li>
        <li><a>Equipment Store</a></li>
      </ul>
    </div>
    <div class="tab-content">
      <div class="gridded-equipments">
        <EquipmentCard v-for="equipment in equipments_in_store" :key="equipment.id" :equipment="equipment"/>
      </div>
    </div>
  </div>
</template>

<script>
import API from '@/api'
import EquipmentCard from '@/components/EquipmentCard'
export default {
  data () {
    return {
      my_heroes: [],
      equipments_in_store: []
    }
  },
  created () {
    this.fetchEquipments()
  },
  methods: {
    fetchEquipments () {
      API.getEquipmentList({}).then(res => {
        this.equipments_in_store = res.data
      }).catch(err => {})
    }
  },
  components: {
    EquipmentCard
  }
}
</script>

<style lang="scss">
.equipment-page {
  .tabs {
    li.is-active {
      border-bottom: 1px solid #FFF;
    }
  }
  .tab-content {
    .gridded-equipments {
      display: grid;
      grid-template-columns: repeat(10, 1fr);
      grid-gap: 10px;
    }
  }
}
</style>
