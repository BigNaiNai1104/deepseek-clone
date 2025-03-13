<template>
  <div class="register-container">
    <div class="register-box">
      <h2>注册</h2>
      <form @submit.prevent="register">
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
        <div class="input-group">
          <label for="confirmPassword">确认密码</label>
          <input 
            v-model="confirmPassword" 
            id="confirmPassword" 
            placeholder="请再次输入密码" 
            type="password" 
            required 
          />
        </div>
        <button type="submit" class="register-button">注册</button>
        <p v-if="errorMessage" class="error-message">{{ errorMessage }}</p>
      </form>
      <div class="login-link">
        <p>已有账号？ <router-link to="/login">立即登录</router-link></p>
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
      confirmPassword: '',
      errorMessage: '',
    };
  },
  methods: {
    async register() {
      // 清除上次的错误信息
      this.errorMessage = '';

      // 检查确认密码是否匹配
      if (this.password !== this.confirmPassword) {
        this.errorMessage = '密码和确认密码不匹配';
        return;
      }

      // 简单的用户名和密码验证
      if (!this.username || !this.password) {
        this.errorMessage = '用户名和密码不能为空';
        return;
      }

      try {
        const response = await axios.post('http://localhost:8000/register', {
          username: this.username,
          password: this.password,
        });

        console.log("注册成功响应:", response);

        // 如果注册成功，跳转到登录页面
        this.$router.push({ name: 'login' });
      } catch (error) {
        console.error("请求失败:", error);  // 输出错误信息
        if (error.response && error.response.data) {
          this.errorMessage = error.response.data.detail || '注册失败，请稍后再试';
        } else {
          this.errorMessage = '注册失败，请稍后再试';
        }
      }
    },
  },
};
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f0f8ff; /* 背景色为浅蓝色 */
}

.register-box {
  background-color: white;
  padding: 40px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  width: 300px;
}

h2 {
  text-align: center;
  color: #1e3a8a; /* 深蓝色 */
  margin-bottom: 20px;
}

.input-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-size: 14px;
  color: #1e3a8a; /* 深蓝色 */
  margin-bottom: 5px;
}

input {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  font-size: 16px;
}

input:focus {
  outline: none;
  border-color: #1e3a8a; /* 聚焦时边框变为深蓝色 */
}

button {
  width: 100%;
  padding: 12px;
  background-color: #1e3a8a; /* 深蓝色按钮 */
  color: white;
  border: none;
  border-radius: 5px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.3s;
}

button:hover {
  background-color: #2563eb; /* 浅蓝色 hover 效果 */
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}

.login-link {
  text-align: center;
  margin-top: 20px;
}

.login-link p {
  font-size: 14px;
}

.login-link a {
  color: #1e3a8a;
  text-decoration: none;
}

.login-link a:hover {
  text-decoration: underline;
}
</style>
