<template>
  <div class="prices-container fluid-container" id="prices">
    <div class="prices-text">
      <h3>материалы и цены</h3>
      <p>
        Наша мастерская имеет возможность применять в производстве не только
        стандартные пластики для FDM печати, такие как ABS/PLA и PETG но и
        инженерные материалы: тугоплавкие, гибкие и композитные пластики
      </p>
    </div>
    <div class="materials-container">
      <div class="slide-button prev-button" role="button">
        <span><font-awesome-icon icon="chevron-left" size="2x"/></span>
      </div>
      <div class="m-glide">
        <div class="glide__track" data-glide-el="track">
          <ul class="glide__slides">
            <li class="glide__slide" v-for="(data, key) in prices" :key="key">
              <MaterialCard :data="data" />
            </li>
          </ul>
        </div>
      </div>
      <div class="slide-button next-button" role="button">
        <font-awesome-icon icon="chevron-right" size="2x" />
      </div>
    </div>
  </div>
</template>

<script>
import prices from "../store/prices";
import MaterialCard from "./MaterialCard";
import Glide from "@glidejs/glide/dist/glide.modular.esm";

// let prevButton;
// let nextButton;
// const screenWidth = window.screen.width;
// let perView;

// if (screenWidth <= 2048 && screenWidth > 992) {
//   perView = 3;
// } else if (screenWidth <= 992) {
//   perView = 1;
// }

// document.addEventListener("DOMContentLoaded", () => {
//   let materialsGlider = new Glide(".m-glide", {
//     perView: perView
//   });
//   prevButton = document.querySelector(".prev-button");
//   nextButton = document.querySelector(".next-button");
//   nextButton.addEventListener("click", function() {
//     materialsGlider.go(">");
//   });
//   prevButton.addEventListener("click", function() {
//     materialsGlider.go("<");
//   });
//   materialsGlider.mount();
// });

export default {
  name: "Prices",
  data: () => ({
    prices: prices
  }),
  components: {
    MaterialCard
  },
  mounted() {
    const prevButton = document.querySelector(".prev-button");
    const nextButton = document.querySelector(".next-button");
    let perView;
    const screenWidth = window.screen.width;
    if (screenWidth <= 2048 && screenWidth > 992) {
      perView = 3;
    } else if (screenWidth <= 992) {
      perView = 1;
    }
    const materialsGlider = new Glide(".m-glide", {
      perView: perView
    });
    nextButton.addEventListener("click", function() {
      materialsGlider.go(">");
    });
    prevButton.addEventListener("click", function() {
      materialsGlider.go("<");
    });
    materialsGlider.mount();
  }
};
</script>

<style scoped>
h3 {
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  color: #352961;
}
.prices-container {
  min-height: 100vh;
  background-color: #f1f3f8;
  display: flex;
  flex-direction: column;
}
.prices-text {
  width: 40vw;
  text-align: start;
  margin-top: 5vh;
  margin-left: 5vw;
  margin-bottom: 5vh;
}
.materials-container {
  display: flex;
  flex-direction: row;
  align-items: stretch;
  justify-content: center;
  margin-bottom: 25px;
}
.slide-button {
  align-self: center;
  color: #fff;
  background-color: #352961;
  height: 50px;
  width: 50px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
}
.slide-button:hover {
  background-color: #523f99;
}
.slide-button span {
  position: relative;
  right: 3px;
}
.m-glide {
  width: 85vw;
}
.glide__slide {
  height: unset;
  align-self: stretch;
  display: flex;
  justify-content: center;
}

@media screen and (max-width: 992px) {
  .prices-text {
    width: 90vw;
    text-align: start;
    margin-top: 5vh;
    margin-left: 5vw;
    margin-bottom: 5vh;
  }
  .slide-button {
    display: none;
  }
  .m-glide {
    width: 95vw;
  }
}
</style>
