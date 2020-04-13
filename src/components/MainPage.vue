<template>
  <div class="container-fluid main-page" id="main">
    <div class="main-page-design-element"></div>
    <Nav></Nav>
    <MainGallery />
  </div>
</template>

<script>
import Nav from "./Nav";
import MainGallery from "./MainGallery";

export default {
  name: "MainPage",
  components: {
    Nav,
    MainGallery
  }
};
</script>

<style scoped>
.main-page {
  min-height: 100vh;
  padding: 0;
  position: relative;
}

.main-page-design-element {
  width: 65vw;
  min-height: 100vh;
  position: absolute;
  top: 0;
  left: 0;
  background-color: #352961;
  z-index: 0;
  border-bottom-right-radius: 300px;
}

@media screen and (max-width: 992px) {
  .main-page-design-element {
    display: none;
  }
  .main-page {
    background-color: #352961;
  }
}
</style>
