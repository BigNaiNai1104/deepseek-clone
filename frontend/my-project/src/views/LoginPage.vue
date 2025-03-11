<template>
  <div>
    <h1>Login Page</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" placeholder="Enter your username" required />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" placeholder="Enter your password" required />
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "LoginPage",
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    async login() {
      try {
        // 使用 URLSearchParams 构造表单数据
        const params = new URLSearchParams();
        params.append('username', this.username);
        params.append('password', this.password);

        const response = await axios.post("http://localhost:8000/token", params, {
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded'
          }
        });
        localStorage.setItem("access_token", response.data.access_token);
        alert("Login successful!");
        this.$router.push("/");  // 登录成功后跳转到首页
      } catch (error) {
        console.error(error);
        const errorMessage = error.response && error.response.data
          ? error.response.data.detail || "Unknown error"
          : "Login failed: Unknown error";
        alert(errorMessage);
      }
    }
  }
};
</script>

<style scoped>
h1 {
  color: #42b983;
}

form {
  max-width: 400px;
  margin: 0 auto;
}

label {
  display: block;
  margin-top: 10px;
}

input {
  width: 100%;
  padding: 8px;
  margin-top: 5px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}
</style>
