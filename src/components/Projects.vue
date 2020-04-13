<template>
  <div class="container-fluid projects-container">
    <div class="projects-design-element"></div>
    <div class="projects-text-container">
      <h3>закажите 3D печать сегодня</h3>
      <p>
        Наша мастерская выполняет заказы на 3D печать функциональных прототипов,
        архитектурных макетов, предметов дизайна и элементов косплея Список
      </p>
      <a href="#contacts" class="btn btn-primary btn-lg">
        Заказать печать
      </a>
    </div>
    <div class="projects-gallery-container">
      <div class="projects-photo-container">
        <img
          src="../assets/projects_gallery/orange.jpg"
          class="img-fluid"
          alt="Responsive image"
        />
        <div class="projects-photo-content">
          <h5>Прототипирование</h5>
          <p>
            Печать функциональных прототипов, корпусных деталей, зубчатых колес,
            запасных частей для бытовой техники.
          </p>
        </div>
      </div>
      <div class="projects-photo-container">
        <img
          src="../assets/projects_gallery/architect.jpg"
          class="img-fluid"
          alt="Responsive image"
        />
        <div class="projects-photo-content">
          <h5>Макетирование</h5>
          <p>
            Изготовление архитектурных макетов и макетов деталей интерьера.
          </p>
        </div>
      </div>
      <div class="projects-photo-container">
        <img
          src="../assets/projects_gallery/headset.jpg"
          class="img-fluid"
          alt="Responsive image"
        />
        <div class="projects-photo-content">
          <h5>Косплей</h5>
          <p>
            Печать элементов косплея, в том числе с установкой электроники.
          </p>
        </div>
      </div>
      <div class="projects-photo-container">
        <img
          src="../assets/mercy.jpg"
          class="img-fluid"
          alt="Responsive image"
        />
        <div class="projects-photo-content">
          <h5>Фанарт</h5>
          <p>
            Печать фигурок и элементов интерьера.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "Projects"
};
</script>

<style scoped>
h3 {
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  color: #352961;
}
.projects-container {
  position: relative;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  padding: 0 !important;
}
.projects-design-element {
  position: absolute;
  width: 45vw;
  height: 80vh;
  right: 0;
  bottom: 0;
  background-color: #352961;
  border-top-left-radius: 200px;
  z-index: 0;
}
.projects-text-container {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  width: 40vw;
  text-align: start;
  margin-top: 5vh;
  margin-left: 5vw;
  margin-bottom: 5vh;
}
.projects-text-container a {
  width: 40%;
  background-color: #352961;
}
.projects-gallery-container {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  padding: 0;
  justify-content: center;
}
.projects-photo-container {
  width: 25%;
  position: relative;
}
.projects-photo-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 54px 15px 15px 15px;
  color: transparent;
  height: 100%;
  width: 100%;
  position: absolute;
  top: 0;
  left: 0;
}
.projects-photo-content p {
  text-align: start;
}
.projects-photo-content:hover {
  background-color: rgba(0, 0, 0, 0.5);
  color: #ffffff;
}

@media screen and (max-width: 992px) {
  .projects-design-element {
    display: none;
  }
  .projects-text-container {
    margin-left: 5vw;
    margin-right: 5vw;
    width: auto;
  }
  .projects-text-container button {
    width: 80%;
  }
  .projects-photo-container {
    width: 90vw;
    margin-bottom: 10px;
  }
  .projects-photo-content {
    background-color: rgba(0, 0, 0, 0.5);
    color: #ffffff;
  }
}
</style>
