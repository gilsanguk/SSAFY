<template>
  <div id="app" class="container">
    <div class="d-flex justify-content-center">
      <h1><b>Coffee Order App</b></h1>
    </div>
    <div class="d-flex gap-3 bg-light rounded-3 p-3 row">
      <MenuList />
      <SizeList />
      <OptionList />
    </div>
    <div class="d-grid gap-2 my-3">
      <button class="btn selected p-2" @click="addOrder">
        장바구니 담기
      </button>
    </div>
    <div>
      <OrderList />
    </div>
  </div>
</template>

<script>
import MenuList from '@/components/MenuList'
import SizeList from '@/components/SizeList'
import OrderList from '@/components/OrderList'
import OptionList from '@/components/OptionList'

export default {
  name: 'App',
  components: {
    MenuList,
    SizeList,
    OrderList,
    OptionList
  },
  methods: {
    addOrder() {
      this.$store.commit('addOrder')
    },
  },
}
</script>

<style>
* {
  box-sizing: border-box;
  font-family: 'Noto Sans KR', sans-serif;
  padding: 0;
  margin: 0;
}

ul {
  list-style: none;
}

.selected{
  background-color: #FFBCB9;
}
</style>
