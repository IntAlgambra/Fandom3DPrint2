<template>
  <div class="material-card">
    <h3>{{ data.material }}</h3>
    <p>{{ data.description }}</p>
    <a class="btn btn-primary" href="#contacts">{{ data.price }}</a>
  </div>
</template>

<script>
export default {
  name: "MaterialCard",
  props: {
    data: Object
  }
};
</script>

<style scoped>
.material-card {
  background-color: #ffffff;
  display: flex;
  flex-direction: column;
  align-items: center;
  /* width: 25vw; */
  border: 1px solid lightgray;
  border-radius: 15px;
  height: 100%;
}
.material-card {
  margin: 0px 10px 0px 10px;
  padding: 20px;
}
.material-card p {
  text-align: start;
  font-size: smaller;
  color: #828082;
}
.material-card h3 {
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  color: #352961;
}
.material-card a {
  margin-bottom: 10px;
  margin-top: auto;
  width: 80%;
  background-color: #352961;
}
</style>
