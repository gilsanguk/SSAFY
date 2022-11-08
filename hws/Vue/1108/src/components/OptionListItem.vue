<template>
  <div
    class="d-flex justify-content-between align-items-center
     border border-1 border-dark rounded-3 m-2 btn"
    style="padding-top:14px; padding-bottom:14px;"
  >
    <span>{{ option.type }}</span>
    <div class="d-flex align-items-center">
      <button
        class="btn btn-secondary border-dark rounded-circle"
        @click="decrease"
        :disabled="option.count === 0"
        style="width:37px"
      >
        -
      </button>
      <span class="px-3">{{ option.count }}</span>
      <button
        class="btn btn-secondary border-dark rounded-circle"
        @click="increase"
        style="width:37px"
      >
        +
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'OptionListItem',
  props: {
    option: Object,
  },
  methods: {
    increase() {
      this.$store.dispatch('increase', this.option)
    },
    decrease() {
      this.$store.dispatch('decrease', this.option)
    },
  },
}
</script>

<style>
</style>