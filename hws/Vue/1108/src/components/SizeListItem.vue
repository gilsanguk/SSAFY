<template>
  <div
    class="d-flex justify-content-between align-items-center
     border border-1 border-dark rounded-3 m-2 btn"
    @click="updateSizeList"
    :class="{ 'selected' : size.selected }"
    style="padding-top:21px; padding-bottom:21px;"
  >
    <span>{{ size.name }}</span>
    <span>{{ size.price }}원</span>
  </div>
</template>

<script>
export default {
  name: 'SizeListItem',
  props: {
    size: Object,
  },
  methods: {
    updateSizeList: function () {
      this.$store.commit('updateSizeList', this.size)
    },
  },
}
</script>

<style>
</style>