import Vue from 'vue'
import Vuex from 'vuex'
import { userList } from './utils/users'
import router from './router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user: localStorage.getItem('user'),
    loggedIn: !!localStorage.getItem('loggedIn')
  },
  mutations: {
    loginSuccess (state, user) {
      state.user = user
      state.loggedIn = true
    },
    loginFailure (state) {
      state.user = null
      state.loggedIn = false
    },
    logout (state) {
      state.user = null
      state.loggedIn = false
    }
  },
  actions: {
    login ({ commit }, { username, password }) {
      let matchedUser = null
      userList.map((user) => {
        if (user.username === username && user.password === password) {
          matchedUser = user
        }
      })
      if (matchedUser !== null) {
        localStorage.setItem('user', matchedUser.username)
        localStorage.setItem('loggedIn', 'true')
        commit('loginSuccess', matchedUser)
        router.push('/')
      } else {
        commit('loginFailure')
      }
    },
    logout ({ commit }) {
      localStorage.removeItem('user')
      localStorage.removeItem('loggedIn')
      commit('logout')
      router.push('/')
    }
  }
})
