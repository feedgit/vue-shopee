<template>
  <div class="main-navigation">
    <div class="container">

      <nav class="navbar" role="navigation" aria-label="main navigation">
        <div class="navbar-brand">
          <router-link :to="{ name: 'Home' }" class="navbar-item">
            <img class="logo" src="/static/img/logo.svg" width="50"/>
            <span class="d-ml has-text-white bold">YouHero</span>
          </router-link>

          <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>

        <div id="navbarBasicExample" class="navbar-menu">
          <div class="navbar-end">
            <div class="navbar-item">
              <div class="" v-if="authentication_user">
                {{authentication_user.username}}
              </div>
              <div class="buttons" v-else>
                <a class="button" @click="$emit('open-login-modal')">Login to build hero house</a>
              </div>

              <div class="dropdown is-right is-hoverable">
                <div class="dropdown-trigger">
                  <a class="" aria-haspopup="true" aria-controls="dropdown-menu4">
                    <img src="/static/icons/more.svg" width="25" />
                  </a>
                </div>
                <div class="dropdown-menu" id="dropdown-menu4" role="menu">
                  <div class="dropdown-content">
                    <a href="#" class="dropdown-item">Profile</a>
                    <a href="#" class="dropdown-item">Log out</a>
                  </div>
                </div>
              </div>

            </div>
          </div>
        </div>
      </nav>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    authentication_user: Object
  },
  data () {
    return {

    }
  }
}
</script>

<style lang="scss">
.main-navigation {
  transition: transform .2s cubic-bezier(.4,0,.2,1),-webkit-transform .2s cubic-bezier(.4,0,.2,1);
  .navbar {
    padding: 10px 0;
    background: none;
    img.logo {
      max-height: none;
    }
    .navbar-start {
      display: flex;
      flex-direction: column;
    }
    .navbar-start, .control {
      width: 100%;
    }
  }
}
</style>
