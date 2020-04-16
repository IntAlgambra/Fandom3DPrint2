<template>
  <div class="container-fluid">
    <AdminPage v-if="isAuthenticated" @logout="onLogout"></AdminPage>
    <AdminLogin v-else @authenticated="getAdminData"></AdminLogin>
  </div>
</template>

<script>
import AdminLogin from "./AdminLogin";
import AdminPage from "./AdminPage";
export default {
  name: "Admin",
  components: {
    AdminLogin,
    AdminPage
  },
  data: () => ({
    isAuthenticated: false
  }),
  methods: {
    async getAdminData() {
      const response = await fetch(
        `${process.env.VUE_APP_API_ENDPOINT}/authasadmin/`
      );
      if (response.status === 200) {
        this.isAuthenticated = true;
      }
    },
    onLogout() {
      this.isAuthenticated = false;
    }
  },
  async mounted() {
    await this.getAdminData();
  }
};
</script>

<style scoped></style>
