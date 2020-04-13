<template>
  <div class="container-fluid contacts-container" id="contacts">
    <div class="contacts-design-element"></div>
    <div class="contacts-text">
      <h3>свяжитесь с нами</h3>
      <p>
        Чтобы заказать 3D печать просто напишите нам в Telegram, Instagram или
        Whatsupp. Наши специалисты проконсультируют вас по вопросам 3D печати и
        произзведут расчет стоимости. Или оставьте свои контакты в форме на
        нашем сайте и мы сами напишем вам на электронную почту
      </p>
      <div class="socials-container">
        <a href="https://t.me/Int_Algambra"
          ><img src="../assets/socials/telegram.svg" alt="telegram icon"
        /></a>
        <a href="#"
          ><img src="../assets/socials/instagram.svg" alt="instagram icon"
        /></a>
        <a href="#"><img src="../assets/socials/vk.svg" alt="vk icon"/></a>
        <a href="#"
          ><img src="../assets/socials/whatsapp.svg" alt="whatsapp icon"
        /></a>
      </div>
    </div>
    <ContactsForm />
  </div>
</template>

<script>
import ContactsForm from "./ContactsForm";
export default {
  name: "Contacts",
  components: {
    ContactsForm
  }
};
</script>

<style scoped>
h3 {
  text-transform: uppercase;
  font-family: "Oswald", sans-serif;
  color: #fff;
}
p {
  color: #fff;
}
.contacts-container {
  min-height: 100vh;
  position: relative;
  padding-top: 10vh;
}
.contacts-design-element {
  height: 80vh;
  width: 50vw;
  position: absolute;
  top: 0;
  left: 0;
  border-bottom-right-radius: 200px;
  background-color: #352961;
  z-index: 1;
}
.contacts-text {
  width: 40vw;
  text-align: start;
  margin-left: 3vw;
  position: relative;
  z-index: 2;
}
.socials-container {
  display: flex;
  justify-content: space-around;
}
@media screen and (max-width: 992px) {
  .contacts-design-element {
    display: none;
  }
  .contacts-container {
    background-color: #352961;
    padding-top: 5vh;
  }
  .contacts-text {
    width: 94vw;
    margin-bottom: 5vh;
    margin-right: 3vw;
    margin-left: auto;
  }
  .socials-container img {
    width: 70%;
  }
}
</style>
