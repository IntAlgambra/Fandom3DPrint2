<template>
  <nav class="navbar navbar-expand-lg">
    <button
      class="navbar-toggler"
      type="button"
      data-toggle="collapse"
      data-target="#navbarTogglerDemo03"
      aria-controls="navbarTogglerDemo03"
      aria-expanded="false"
      aria-label="Toggle navigation"
    >
      <font-awesome-icon icon="bars" size="lg" />
    </button>
    <a class="navbar-brand d-lg-none" href="#"
      ><img src="../assets/logo.png" width="50" height="50" alt=""
    /></a>

    <div class="collapse navbar-collapse " id="navbarTogglerDemo03">
      <ul class="navbar-nav ml-auto mt-2 mt-lg-0">
        <li class="nav-item white-nav-item">
          <a class="nav-link" href="#main"><span>домой</span></a>
        </li>
        <li class="nav-item white-nav-item">
          <a class="nav-link" href="#projects"><span>проекты</span></a>
        </li>
        <li class="nav-item colored-nav-item">
          <a class="nav-link" href="#prices"><span>цены</span></a>
        </li>
        <li class="nav-item colored-nav-item">
          <a class="nav-link" href="#contacts"><span>контакты</span></a>
        </li>
      </ul>
    </div>
    <a class="navbar-brand d-none d-lg-block" href="#"
      ><img src="../assets/logo.png" class="main-logo-img" alt="logo"
    /></a>
  </nav>
</template>

<script>
export default {
  name: "Nav",
  data: () => ({
    image: require("../assets/logo.png")
  })
};
</script>

<style scoped>
.navbar {
  padding-left: 0px;
  padding-right: 0px;
  font-family: "Oswald", sans-serif;
}

.navbar-brand {
  margin-right: 2vw;
}

.nav-item {
  width: 11vw;
  text-transform: uppercase;
}

.nav-item span {
  border-bottom: 3px solid transparent;
}

.colored-nav-item a {
  color: #352961;
}

.white-nav-item span:hover {
  border-bottom: 3px solid #fff;
}

.colored-nav-item span:hover {
  border-bottom: 3px solid #352961;
}

.nav-item .btn {
  background-color: #352961;
  width: 80%;
}

.main-logo-img {
  width: 8vw;
}

@media screen and (max-width: 992px) {
  .navbar {
    background-color: #fff;
  }
  .nav-item {
    width: 100%;
  }
  .nav-item a {
    color: #352961;
  }
}

.navbar-toggler {
  z-index: 2;
  color: #352961;
}

.nav-link {
  color: #fff;
}
</style>
