<template>
  <div class="home-container">
    <h1>Welcome to DeepSeek Clone</h1>
    <div v-if="isAuthenticated" class="welcome-message">
      <p>Welcome, {{ user.username }}!</p>
      <button @click="logout" class="btn-logout">Logout</button>
    </div>
    <div v-else class="login-prompt">
      <p>Please log in to continue.</p>
      <router-link to="/login" class="btn-login">Login</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "HomePage",
  computed: {
    ...mapGetters(["isAuthenticated", "getUser"])
  },
  methods: {
    ...mapActions(["logout"]),
  }
};
</script>

<style scoped>
.home-container {
  text-align: center;
  padding: 40px;
  background: linear-gradient(to right, #6a11cb, #2575fc); /* 背景渐变 */
  color: white;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

h1 {
  font-size: 3rem;
  margin-bottom: 20px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* 增加标题阴影 */
}

.welcome-message p {
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.login-prompt p {
  font-size: 1.5rem;
  margin-bottom: 20px;
}

.btn-logout, .btn-login {
  padding: 15px 30px;
  font-size: 18px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  display: inline-block;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 按钮阴影 */
  transition: all 0.3s ease;
}

.btn-logout:hover, .btn-login:hover {
  background-color: #45a049;
  transform: translateY(-2px); /* 鼠标悬浮时按钮上升 */
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2); /* 鼠标悬浮时按钮阴影变大 */
}

a {
  text-decoration: none;
  color: white;
}

a:hover {
  text-decoration: underline;
}
</style>
