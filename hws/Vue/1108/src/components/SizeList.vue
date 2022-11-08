<template>
  <div class="bg-white rounded-3 p-3 col">
    <h4><b>2. 사이즈를 고르세요.</b></h4>
    <div>
      <MenuListItem
        v-for="size in sizeList"
        :key="size.id"
        :size="size"
      />
    </div>
  </div>
</template>

<script>
import MenuListItem from '@/components/SizeListItem'

export default {
  name: 'SizeList',
  components: {
    MenuListItem,
  },
  computed: {
    sizeList: function () {
       return this.$store.state.sizeList
    },
  },
}
</script>

<style>
</style>