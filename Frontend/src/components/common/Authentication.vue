<template>
  <form class="authentication" @submit.prevent="logIn">
    <span>You need an account to build your hero house</span>
    <div class="field">
      <label class="label has-text-white">username</label>
      <div class="control">
        <input v-model="credentials.username" class="input" type="text" placeholder="Enter your username">
      </div>
    </div>

    <div class="field">
      <label class="label has-text-white">password</label>
      <div class="control">
        <input v-model="credentials.password" class="input" type="password" placeholder="Enter your password">
      </div>
    </div>

    <div class="field is-grouped is-grouped-right">
      <p class="control">
        <a class="button" @click="logIn">Continue / Register</a>
      </p>
    </div>
  </form>
</template>

<script>
import API from '@/api'
import Cookies from 'js-cookie'
import session from '@/api/session'
export default {
  data () {
    return {
      credentials: {
        username: 'lecongtoan',
        password: 'chelsea39'
      },
      is_logging_in: false
    }
  },
  methods: {
    logIn () {
      this.is_logging_in = true
      API.logIn(this.credentials).then(res => {
        if (res.data.token) {
          Cookies.set('token', res.data.token, { expires: 365 })
          session.defaults.headers.Authorization = `JWT ${res.data.token}`
          this.$emit('close-login-modal')
        } else {
          this.$swal(`Error!`, `Can't login right now. Please contact administrator: congtoanle7@gmail.com`, `error`)
        }
      }).catch(err => {
        console.log(err);
        this.$swal(`Error!`, `Can't login right now. Please contact administrator: congtoanle7@gmail.com`, `error`)
      })
    }
  }
}
</script>

<style lang="css" scoped>
</style>
