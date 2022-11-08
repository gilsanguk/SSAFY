import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    orderList: [],
    menuList: [
      {
        name: '아메리카노',
        price: 4500,
        selected: true,
        image: 'https://source.unsplash.com/featured/?americano'
      },
      {
        name: '플레인요거트스무디',
        price: 5500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?yogurt'
      },
      {
        name: '자바칩 프라푸치노',
        price: 6500,
        selected: false,
        image: 'https://source.unsplash.com/featured/?coffee'
      },
    ],
    sizeList: [
      {
        name: 'tall',
        price: 0,
        selected: true
      },
      {
        name: 'grande',
        price: 500,
        selected: false
      },
      {
        name: 'venti',
        price: 1000,
        selected: false
      }
    ],
    optionList: [
      {
        type: '샷',
        price: 500,
        count: 0,
      },
      {
        type: '바닐라 시럽',
        price: 300,
        count: 0,
      },
      {
        type: '카라멜 시럽',
        price: 100,
        count: 0,
      }
    ]
  },
  getters: {
    totalOrderCount(state) {
      return state.orderList.length
    },
    totalOrderPrice(state) {
      const total = state.orderList.reduce((acc, order) => {
        return acc + order.menu.price + order.size.price + order.options.reduce((acc, option) => {
          return acc + option.price * option.count
        }, 0)
      }, 0)
      return total
    }
  },
  mutations: {
    addOrder(state) {
      const order = {
        menu: state.menuList.find(menu => menu.selected),
        size: state.sizeList.find(size => size.selected),
        options: state.optionList.map(option => {
          return {
            type: option.type,
            price: option.price,
            count: option.count
          }
        })
      }
      state.orderList.push(order);
    },
    updateMenuList(state, selectedMenu) {
      state.menuList.forEach(menu => {
        menu.selected = menu.name === selectedMenu.name
      })
    },
    updateSizeList(state, selectedSize) {
      state.sizeList.forEach(size => {
        size.selected = size.name === selectedSize.name
      })
    },
    updateOptionList(state, newOption) {
      const selectedOption = state.optionList.find(option => option.type === newOption.type)
      selectedOption.count = newOption.count
    }
  },
  actions: {
    increase(context, newOption) {
      newOption.count++;
      context.commit('updateOptionList', newOption)
    },
    decrease(context, newOption) {
      newOption.count--;
      context.commit('updateOptionList', newOption)
    }
  },
  modules: {
  }
})