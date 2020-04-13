<template>
  <div class="container-fluid">
    <MainPage />
    <Projects id="projects" />
    <Prices />
    <Contacts />
  </div>
</template>

<script>
import MainPage from "./MainPage";
import Projects from "./Projects";
import Prices from "./Prices";
import Contacts from "./Contacts";

export default {
  name: "Client",
  components: {
    MainPage,
    Projects,
    Prices,
    Contacts
  },
  mounted() {
    if (this.$route.hash) {
      location.hash = this.$route.hash;
    }
  }
};
</script>

<style scoped>
div {
  padding: 0;
  margin: 0;
}
</style>
