<template>
  <img @error="loadDefault" :src="src ? src : '/static/no-image.png'" :width="width" :height="height" />
</template>

<script>
export default {
  props: ['src', 'width', 'height'],
  methods: {
    loadDefault: function (e) {
      e.target.src = '/static/no-image.png'
    }
  }
}
</script>
<style>
img.cover {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
</style>
