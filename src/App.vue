<template>
  <div id="app">
    <vue-ins-progress-bar/>
    <AppHeader @open-login-modal="$refs.login_modal.open()" :authentication_user="authentication_user"/>
    <AppNavigator/>
    <main>
      <router-view></router-view>
    </main>
    <AppFooter/>
    <sweet-modal ref="login_modal" modal-theme="dark" overlay-theme="dark" title="Login to YouHero">
    	<Authentication @close-login-modal="$refs.login_modal.close()"/>
    </sweet-modal>
  </div>
</template>

<script>
import AppHeader from '@/components/common/Header'
import AppFooter from '@/components/common/Footer'
import AppNavigator from '@/components/common/Navigator'
import { SweetModal, SweetModalTab } from 'sweet-modal-vue'
import Authentication from '@/components/common/Authentication'
import Cookies from 'js-cookie'
var jwtDecode = require('jwt-decode')
export default {
  name: 'app',
  data () {
    return {
      authentication_user: null
    }
  },
  created () {
    this.initAuthenticatedUser()
  },
  methods: {
    initAuthenticatedUser () {
      var token = Cookies.get('token')
      if (token) {
          this.authentication_user = jwtDecode(token)
      }
    }
  },
  components: {
    AppHeader,
    AppFooter,
    AppNavigator,
    Authentication,
    SweetModal,
		SweetModalTab
  }
}
</script>

<style lang="scss">
@import 'assets/bulma.css';
.bg-div {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
}
</style>
