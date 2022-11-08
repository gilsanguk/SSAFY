<template>
  <div class="bg-white rounded-3 p-3 col">
    <h4><b>1. 음료를 고르세요.</b></h4>
    <div>
      <MenuListItem
        v-for="menu in menuList"
        :key="menu.id"
        :menu="menu"
      />
    </div>
  </div>
</template>

<script>
import MenuListItem from '@/components/MenuListItem'

export default {
  name: 'MenuList',
  components: {
    MenuListItem
  },
  computed: {
    menuList: function () {
      return this.$store.state.menuList
    },
  },
  methods: {
    selectMenu: function () {
    },
  },
}
</script>

<style>

</style>