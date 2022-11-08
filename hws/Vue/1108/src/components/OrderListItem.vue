<template>
  <li class="list-unstyled">
    <div class="d-flex justify-content-between">
      <div class="d-flex">
        <img :src="order.menu.image" style="height:50px; width:50px" class="rounded-3">
        <div class="ms-3">
          <p class="m-0">{{ order.menu.name }}</p>
          <p class="m-0">사이즈: {{ order.size.name }}</p>
        </div>
      </div>
      <div>
        <p class="m-0">가격: {{ orderPrice }}원</p>
        <p class="m-0">
          <span
            v-for="option in order.options"
            :key="option.type"
          >
            {{ option.type }} {{ option.count }} |
          </span>
        </p>
      </div>
    </div>
    <hr>
  </li>
</template>

<script>
export default {
  name: 'OrderListItem',
  props: {
    order: Object,
  },
  computed: {
    orderPrice() {
      return (
        this.order.menu.price + 
        this.order.size.price +
        this.order.options.reduce((acc, cur) => acc + cur.price * cur.count, 0)
      )
    },
  },
}
</script>

<style>
</style>