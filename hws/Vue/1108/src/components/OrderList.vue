<template>
  <div>
    <div class="d-flex bg-light rounded-3 p-3 row">
      <h3><b>주문 내역</b></h3>
      <p><b>총 {{ totalOrderCount }}건: {{ totalOrderPrice }}</b></p>
      <OrderListItem
        v-for="order in orderList"
        :key="order.id"
        :order="order"
      />
    </div>
  </div>
</template>

<script>
import OrderListItem from '@/components/OrderListItem'

export default {
  name: 'OrderList',
  components: {
    OrderListItem,
  },
  computed: {
    orderList() {
      return this.$store.state.orderList
    },
    totalOrderCount() {
      return this.$store.getters.totalOrderCount
    },
    totalOrderPrice() {
      return this.$store.getters.totalOrderPrice
    },
  },
}
</script>

<style>
</style>