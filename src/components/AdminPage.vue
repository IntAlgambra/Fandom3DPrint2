<template>
  <div class="container">
    <button type="button" class="btn btn-danger" id="logout" @click="logout">
      Выйти
    </button>
    <div class="card" v-for="item in questions" :key="item.id">
      <div class="card-body">
        <h5 class="card-title">{{ item.email }}</h5>
        <p class="card-text">
          {{ item.question }}
        </p>
        <a :href="genFileHref(item.id)" class="btn btn-primary" download>
          Скачать файл
        </a>
        <button
          type="button"
          class="btn btn-danger"
          @click="deleteQuestion(item.id)"
        >
          Удалить ввопрос
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminPage",
  data: () => ({
    questions: null
  }),
  methods: {
    async logout() {
      const response = await fetch(
        `${process.env.VUE_APP_API_ENDPOINT}/logout/`
      );
      if (response.status === 200) {
        this.$emit("logout");
      }
    },
    async deleteQuestion(id) {
      const response = await fetch(
        `${process.env.VUE_APP_API_ENDPOINT}/question/${id}`,
        {
          method: "delete"
        }
      );
      if (response.status === 200) {
        this.questions = this.questions.filter(item => item.id !== id);
      }
    },
    genFileHref(id) {
      return `${process.env.VUE_APP_API_ENDPOINT}/question/file/${id}`;
    }
  },
  async mounted() {
    const response = await fetch(
      `${process.env.VUE_APP_API_ENDPOINT}/question/`
    );
    this.questions = await response.json();
  }
};
</script>

<style scoped>
.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 50px;
  width: 50vw;
}
.card {
  width: 100%;
  margin-bottom: 50px;
}
.btn {
  margin-right: 25px;
}
#logout {
  align-self: flex-start;
  margin-bottom: 50px;
}
</style>
