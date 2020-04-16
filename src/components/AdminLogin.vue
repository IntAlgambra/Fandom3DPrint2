<template>
  <div class="container admin-login-container">
    <div class="card" style="width: 18rem;">
      <div class="card-body">
        <h5 class="card-title">Login as admin</h5>
        <form>
          <div class="form-group">
            <label for="login-input">Login</label>
            <input type="text" class="form-control" id="login-input" />
          </div>
          <div class="form-group">
            <label for="password-input">Password</label>
            <input type="password" class="form-control" id="password-input" />
          </div>
          <div v-if="isCredentialsInvalid">Wrong login or password</div>
          <button type="submit" class="btn btn-primary" @click="sendData">
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AdminLoginForm",
  data: () => ({
    isCredentialsInvalid: false
  }),
  methods: {
    async sendData(e) {
      e.preventDefault();
      const password = document.querySelector("#password-input").value;
      const login = document.querySelector("#login-input").value;
      const data = new FormData();
      data.append("login", login);
      data.append("password", password);
      const response = await fetch(
        `${process.env.VUE_APP_API_ENDPOINT}/login/`,
        {
          method: "post",
          body: data
        }
      );
      if (response.status === 200) {
        this.$emit("authenticated");
      } else {
        this.isCredentialsInvalid = true;
      }
    }
  }
};
</script>

<style scoped>
.admin-login-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
