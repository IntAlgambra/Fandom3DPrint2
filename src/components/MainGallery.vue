<template>
  <div class="main-gallery-container">
    <div class="main-gallery-text-container">
      <h3>закажите 3D печать сегодня</h3>
      <p>
        Наша мастерская выполняет заказы на 3D печать функциональных прототипов,
        архитектурных макетов, предметов дизайна и элементов косплея Список
        доступных материалов включает в себя как стандартные PLA, ABS и PETG
        пластики, так и инженерные угле- и стеклонаполненные композиты
      </p>
      <a href="#contacts" class="btn btn-outline-light btn-lg">
        Заказать печать
      </a>
    </div>
    <div class="main-gallery-text-mobile">
      <h3>закажите 3D печать сегодня</h3>
      <p>
        Наша мастерская выполняет заказы на 3D печать функциональных прототипов,
        архитектурных макетов, предметов дизайна и элементов косплея.
      </p>

      <a href="#contacts" class="btn btn-outline-light btn-lg">
        Заказать печать
      </a>
    </div>
    <div class="main-gallery-photo-container glide">
      <div class="photo-container glide__track shadow-lg" data-glide-el="track">
        <ul class="glide__slides">
          <li class="glide__slide">
            <img
              src="../assets/main_gallery/sbase.jpg"
              class="img-fluid"
              alt="Responsive image"
            />
          </li>
          <li class="glide__slide">
            <img
              src="../assets/main_gallery/pumpkin.jpg"
              class="img-fluid"
              alt="Responsive image"
            />
          </li>
          <li class="glide__slide">
            <img
              src="../assets/main_gallery/venera.jpg"
              class="img-fluid"
              alt="Responsive image"
            />
          </li>
          <li class="glide__slide">
            <img
              src="../assets/main_gallery/fox.jpg"
              class="img-fluid"
              alt="Responsive image"
            />
          </li>
        </ul>
      </div>
      <div class="gallery-buttons-container" data-glide-el="controls">
        <div
          class="gallery-button gallery-prev"
          role="button"
          data-glide-dir="<"
        >
          <font-awesome-icon icon="chevron-left" size="lg" />
        </div>
        <div
          class="gallery-button gallery-next"
          role="button"
          data-glide-dir=">"
        >
          <font-awesome-icon icon="chevron-right" size="lg" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Glide, { Controls, Swipe } from "@glidejs/glide/dist/glide.modular.esm";

// document.addEventListener("DOMContentLoaded", () => {
//   new Glide(".glide").mount({ Controls, Swipe });
// });

export default {
  name: "MainGallery",
  mounted() {
    new Glide(".glide").mount({ Controls, Swipe });
  }
};
</script>

<style scoped>
h3 {
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
}
p {
  font-family: "Open Sans", sans-serif;
}
.main-gallery-container {
  position: relative;
  z-index: 2;
  display: flex;
  flex-wrap: wrap;
  margin-left: 7vw;
}
.main-gallery-text-container {
  text-align: start;
  width: 40vw;
  color: #fff;
  margin-right: 5vw;
  padding-top: 5vh;
}
.main-gallery-text-mobile {
  display: none;
}
.main-gallery-photo-container {
  position: relative;
  width: 26vw;
}
.photo-container ul {
  margin: 0;
}
.main-gallery-photo-container img {
  border-radius: 65px 5px 5px 5px;
}
.gallery-buttons-container {
  display: flex;
  flex-direction: row;
  width: 40%;
  height: 36px;
  position: relative;
  left: 30%;
  bottom: 18px;
}
.gallery-button {
  background-color: #dc3545;
  flex-grow: 1;
  color: #fff;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}
.gallery-button:hover {
  background-color: #c02b39;
}
.gallery-prev {
  border-top-left-radius: 10px;
  border-bottom-left-radius: 10px;
}
.gallery-next {
  border-top-right-radius: 10px;
  border-bottom-right-radius: 10px;
}

@media screen and (max-width: 992px) {
  .main-gallery-container {
    margin-left: 5vw;
    margin-right: 5vw;
  }
  .main-gallery-text-container {
    display: none;
  }
  .main-gallery-text-mobile {
    display: flex;
    flex-direction: column;
    color: #fff;
    width: 90vw;
    margin-top: 5vh;
    margin-bottom: 5vh;
    text-align: start;
  }
  .main-gallery-photo-container {
    width: 90vw;
  }
}
</style>
