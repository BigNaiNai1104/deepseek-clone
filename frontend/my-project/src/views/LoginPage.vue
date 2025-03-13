<template>
  <div class="login-container">
    <div class="login-box">
      <h2>登录</h2>
      <form @submit.prevent="login">
        <div class="input-group">
          <label for="username">用户名</label>
          <input 
            v-model="username" 
            id="username" 
            placeholder="请输入用户名" 
            type="text" 
            required 
          />
        </div>
        <div class="input-group">
          <label for="password">密码</label>
          <input 
            v-model="password" 
            id="password" 
            placeholder="请输入密码" 
            type="password" 
            required 
          />
        </div>
        <button type="submit" class="login-button">登录</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
      <div class="register-link">
        <p>没有账号？ <router-link to="/register">立即注册</router-link></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      errorMessage: '',
    };
  },
  methods: {
    async login() {
      // 清除上次的错误信息
      this.errorMessage = '';
      
      // 简单的用户名和密码验证
      if (!this.username || !this.password) {
        this.errorMessage = '用户名和密码不能为空';
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/login', {
          username: this.username,
          password: this.password,
        });

        console.log("后端响应:", response);  // 输出响应内容

        if (response.data.token) {
          localStorage.setItem('access_token', response.data.token);
          this.$router.push({ name: 'profile' });
        } else {
          this.errorMessage = '登录失败，请稍后再试';
        }
      } catch (error) {
        console.error("请求失败:", error);  // 输出错误信息
        if (error.response && error.response.data) {
          this.errorMessage = error.response.data.detail || '用户名或密码错误';
        } else {
          this.errorMessage = '登录失败，请稍后再试';
        }
      }
    },
  },
};
</script>
