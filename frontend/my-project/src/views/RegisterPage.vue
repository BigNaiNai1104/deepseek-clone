<template>
  <div>
    <h1>Register Page</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Username:</label>
        <input type="text" id="username" v-model="username" placeholder="Enter your username" />
      </div>
      <div>
        <label for="email">Email:</label>
        <input type="email" id="email" v-model="email" placeholder="Enter your email" />
      </div>
      <div>
        <label for="password">Password:</label>
        <input type="password" id="password" v-model="password" placeholder="Enter your password" />
      </div>
      <button type="submit">Register</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "RegisterPage",
  data() {
    return {
      username: "",
      email: "",
      password: ""
    };
  },
  methods: {
    async register() {
      try {
        // 修改请求路径为 /users/
        await axios.post("http://localhost:8000/users/", {
          username: this.username,
          email: this.email,
          password: this.password
        });
        alert("Registration successful!");
        this.$router.push("/login");  // 注册成功后跳转到登录页面
      } catch (error) {
        console.error(error);
        alert("Registration failed: " + error.response.data.detail);
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
