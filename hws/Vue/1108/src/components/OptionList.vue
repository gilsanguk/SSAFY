<template>
  <div class="bg-white rounded-3 p-3 col">
    <h4><b>3. 옵션을 고르세요.</b></h4>
    <div>
      <OptionListItem
        v-for="option in optionList"
        :key="option.id"
        :option="option"
      />
    </div>
  </div>
</template>

<script>
import OptionListItem from '@/components/OptionListItem'

export default {
  name: 'OptionList',
  components: {
    OptionListItem,
  },
  computed: {
    optionList() {
      return this.$store.state.optionList
    },
  },
  methods: {
    increase: function () {
    },
    decrease: function () {
    },
  },
}
</script>

<style>
</style>