<template>
  <div class="login-container">
    <form @submit.prevent="login">
      <h2>Login</h2>
      <div class="input-group">
        <input 
          type="text" 
          v-model="username" 
          placeholder="Username" 
          required 
          class="input-field"
        />
      </div>
      <div class="input-group">
        <input 
          type="password" 
          v-model="password" 
          placeholder="Password" 
          required 
          class="input-field"
        />
      </div>
      <button type="submit" class="btn">Login</button>
      <p class="error-message" v-if="loginError">Invalid username or password</p>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      loginError: false,
    };
  },
  methods: {
    async login() {
      this.loginError = false;
      try {
        const response = await axios.post('http://localhost:8000/token', {
          username: this.username,
          password: this.password,
        });
        const { access_token } = response.data;
        localStorage.setItem('access_token', access_token);
        this.$router.push({ name: 'home' });
      } catch (error) {
        this.loginError = true;
        console.error('Login failed:', error);
      }
    },
  },
};
</script>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background-color: #f7f7f7;
}

form {
  background-color: white;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  width: 300px;
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
}

.input-field {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.btn {
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #45a049;
}

.error-message {
  color: red;
  text-align: center;
  font-size: 14px;
  margin-top: 10px;
}
</style>
