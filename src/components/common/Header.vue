<template>
  <div class="main-navigation">
    <nav class="breadcrumb is-small has-bullet-separator" aria-label="breadcrumbs">
      <ul class="">
        <li><a href="#" class="has-text-white">Seller Centre</a></li>
        <li><a href="#" class="has-text-white">Download</a></li>
        <li><a href="#" class="has-text-white">Follow us on</a></li>
      </ul>
    </nav>

    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="navbar-brand">
        <a class="navbar-item" href="/">
          <img src="/static/img/logo.png">
        </a>

        <a role="button" class="navbar-burger burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div id="navbarBasicExample" class="navbar-menu">
        <div class="navbar-start">
          <div class="control">
            <input class="input" type="text" placeholder="Search products ...">
          </div>
        </div>

        <div class="navbar-end">
          <div class="navbar-item">
            <div class="buttons">
              <a>
                <img src="/static/img/app-icons/cart.svg"/>
              </a>
            </div>
          </div>
        </div>
      </div>
    </nav>
  </div>
</template>

<script>
export default {
}
</script>

<style lang="scss">
.main-navigation {
  background: linear-gradient(-180deg,#f53d2d,#f63);
  transition: transform .2s cubic-bezier(.4,0,.2,1),-webkit-transform .2s cubic-bezier(.4,0,.2,1);
  color: #FFF;
  .breadcrumb {
    margin-bottom: 0;
  }
  .navbar {
    background: none;
  }
}
</style>
