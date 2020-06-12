<template>
  <div class="section">
    <div class="container">
      <div class="columns is-centered">
        <div class="column is-6">
          <div class="box">
            <h1 class="title is-2">Login</h1>
            <hr class="hr">
            <form class="form" @submit="login({username, password})" @submit.prevent>
              <div class="field">
                <label for="username" class="label">Username</label>
                <div class="control">
                  <input v-model="username" type="text" id="username" name="username" class="input" required>
                </div>
              </div>
              <div class="field">
                <label for="password" class="label">Password</label>
                <div class="control">
                  <input v-model="password" type="password" id="password" name="password" class="input" required>
                </div>
              </div>
              <div class="field">
                <button class="button is-dark">Login</button>
              </div>
              <p><a><small @click="normalUser">Normal user: normaluser/normaluser</small></a></p>
              <p><a><small @click="betaUser">Beta user: betauser/betauser</small></a></p>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import { mapActions } from 'vuex'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    normalUser: function () {
      this.username = 'normaluser'
      this.password = 'normaluser'
    },
    betaUser: function () {
      this.username = 'betauser'
      this.password = 'betauser'
    },
    ...mapActions([
      'login'
    ])
  }
}
</script>
