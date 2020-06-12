<template>
  <b-navbar :type="headerColor" id="nav">
    <template slot="brand">
      <b-navbar-item href="/">
        <strong>HN</strong>
      </b-navbar-item>
      <b-navbar-item v-if="isBeta">
        <i>Beta tester</i>
      </b-navbar-item>
    </template>
    <template slot="start">
      <b-navbar-item href="/">
        Hot
      </b-navbar-item>
      <b-navbar-item href="/ask">
        Ask
      </b-navbar-item>
      <b-navbar-item href="/show">
        Show
      </b-navbar-item>
    </template>
    <template slot="end">
      <b-navbar-item tag="div">
        <div class="buttons">
          <a class="button is-black" v-if="loggedIn" @click="logout">
            Log out
          </a>
          <a class="button is-black" v-else href="/login">
            Log in
          </a>
        </div>
      </b-navbar-item>
    </template>
  </b-navbar>
</template>
<style lang="stylus">
#nav {
  margin-bottom: 15px
}
</style>
<script>
import { mapState, mapActions } from 'vuex'
import { betaAccess } from '../utils/users'

export default {
  data () {
    return {
      headerColor: 'is-dark',
      isBeta: betaAccess()
    }
  },
  methods: {
    ...mapActions([
      'logout'
    ])
  },
  computed: mapState([
    'loggedIn'
  ])
}
</script>
