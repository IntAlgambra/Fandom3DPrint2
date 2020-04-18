<template>
  <div class="form-container">
    <form id="contacts-form" @submit="sendData" novalidate>
      <div class="form-group">
        <label for="email-input">Email</label>
        <input
          type="email"
          class="form-control"
          id="email-input"
          aria-describedby="emailHelp"
          @change="validateEmail"
        />
        <div class="invalid-feedback">
          Please enter correct email.
        </div>
        <small id="emailHelp" class="form-text text-muted"
          >Мы никому не передадим ваш адрес email</small
        >
      </div>
      <div class="form-group">
        <label for="question-input">Ваше сообщение</label>
        <textarea
          class="form-control"
          id="question-input"
          rows="3"
          @change="validateQuestion"
        ></textarea>
      </div>
      <div class="custom-file">
        <input
          type="file"
          class="custom-file-input"
          id="file-input"
          @change="validateFile"
        />
        <label class="custom-file-label" for="file-input">{{ filename }}</label>
        <div class="invalid-feedback">Wronge file format</div>
        <div class="valid-feedback">Файл выбран</div>
      </div>
      <vue-recaptcha
        ref="recaptcha"
        :sitekey="captchaKey"
        :loadRecaptchaScript="true"
        @verify="checkToken"
        @expired="onCaptchaExpired"
      ></vue-recaptcha>
      <div class="submit-group">
        <button type="submit" class="btn btn-primary">
          Отправить
        </button>
        <div class="submit-success">Отправлено успешно!</div>
        <div class="submit-failed">Не отправлено!</div>
      </div>
    </form>
  </div>
</template>

<script>
import VueRecaptcha from "vue-recaptcha";

const ALLOWED_EXTENSIONS = ["stl", "3mf", "obj", "prt", "dwg", "pdf", "dxf"];

export default {
  name: "ContactsForm",
  data: () => ({
    filename: "Choose file",
    endpoint: "question/",
    captchaToken: null,
    captchaKey: process.env.VUE_APP_RECAPTCHA_KEY
  }),
  components: { VueRecaptcha },
  methods: {
    checkToken(token) {
      this.captchaToken = token;
    },
    onCaptchaExpired() {
      this.$refs.recaptcha.reset();
    },
    validateField(field, condition) {
      if (condition) {
        field.classList.remove("is-invalid");
        field.classList.add("is-valid");
        return true;
      } else {
        field.classList.remove("is-valid");
        field.classList.add("is-invalid");
        return false;
      }
    },
    validateEmail() {
      const emailInput = document.querySelector("#email-input");
      const email = String(emailInput.value);
      const emailRe = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
      return this.validateField(emailInput, emailRe.test(email.toLowerCase()));
    },
    validateQuestion() {
      const questionInput = document.querySelector("#question-input");
      return this.validateField(questionInput, questionInput.value);
    },
    validateFile() {
      const fileInput = document.querySelector("#file-input");
      if (fileInput.files.length === 0) {
        return true;
      }
      const extension = fileInput.files[0].name.split(".")[1];
      if (
        this.validateField(
          fileInput,
          ALLOWED_EXTENSIONS.includes(extension.toLowerCase())
        )
      ) {
        this.filename = fileInput.files[0].name;
        return true;
      } else {
        return false;
      }
    },
    async sendData(event) {
      event.preventDefault();
      const isEmailValid = this.validateEmail();
      const isQuestionValid = this.validateQuestion();
      const isFileValid = this.validateFile();
      if (isEmailValid && isQuestionValid && isFileValid && this.captchaToken) {
        const data = new FormData();
        const fileInput = document.querySelector("#file-input");
        const email = document.querySelector("#email-input").value;
        const question = document.querySelector("#question-input").value;
        data.append("email", email);
        data.append("question", question);
        if (fileInput.files.length !== 0) {
          data.append("file", fileInput.files[0], fileInput.files[0].name);
        }
        data.append("captcha_token", this.captchaToken);
        const response = await fetch(this.endpoint, {
          method: "post",
          body: data
        });
        if (response.status === 201) {
          this.showSuccess();
        } else {
          this.showFailure();
        }
        this.resetForm();
      }
    },
    showSuccess() {
      const successMsg = document.querySelector(".submit-success");
      successMsg.setAttribute("style", "display: flex;");
      setTimeout(() => {
        successMsg.setAttribute("style", "display: none;");
      }, 2000);
    },
    showFailure() {
      const failureMsg = document.querySelector(".submit-failed");
      failureMsg.setAttribute("style", "display: flex;");
      setTimeout(() => {
        failureMsg.setAttribute("style", "display: none;");
      }, 2000);
    },
    resetForm() {
      const inputs = [
        document.querySelector("#file-input"),
        document.querySelector("#email-input"),
        document.querySelector("#question-input")
      ];
      inputs.forEach(item => {
        item.value = "";
        item.classList.remove("is-invalid");
        item.classList.remove("is-valid");
      });
      this.filename = "";
    }
  }
};
</script>

<style scoped>
.form-container {
  position: absolute;
  top: 15vh;
  right: 5vw;
  border: 1px solid lightgray;
  border-radius: 15px;
  z-index: 2;
  width: 40vw;
  text-align: start;
  padding: 15px;
}
.form-container button {
  background-color: #352961;
}
.custom-file {
  margin-bottom: 15px;
}
.submit-group {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  margin-top: 15px;
}
.submit-group div {
  margin-left: 15px;
  display: none;
}
.submit-success {
  color: green;
}
.submit-failed {
  color: red;
}
@media screen and (max-width: 992px) {
  .form-container {
    position: static;
    width: 90vw;
    text-align: start;
    padding: 15px;
    background-color: #fff;
    margin-right: 5vw;
  }
}
</style>
