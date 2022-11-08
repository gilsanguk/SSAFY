<template>
  <div
    class="d-flex justify-content-between align-items-center
     border border-1 border-dark rounded-3 m-2 p-2 btn"
    @click="updateMenuList"
    :class="{ 'selected' : menu.selected }"
  >
    <img :src="menu.image" style="height:50px; width:50px" class="rounded-3">
    <span>{{ menu.name }}</span>
    <span>{{ menu.price }}원</span>
  </div>
</template>

<script>
export default {
  name: 'MenuListItem',
  props: {
    menu: Object,
  },
  methods: {
    updateMenuList: function () {
      this.$store.commit('updateMenuList', this.menu)
    },
  },
}
</script>

<style>
</style>