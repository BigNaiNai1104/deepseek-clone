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
      
      // 假设这里是登录逻辑
      const loginSuccess = this.username === 'admin' && this.password === '123456'; // 模拟登录验证
      if (loginSuccess) {
        // 存储 token 信息
        localStorage.setItem('access_token', 'your-token-here');
        
        // 跳转到个人资料页面
        this.$router.push({ name: 'profile' });
      } else {
        this.errorMessage = '用户名或密码错误';
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
  height: 100vh;
  background-color: #f0f8ff; /* 背景色为浅蓝色 */
}

.login-box {
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

.register-link {
  text-align: center;
  margin-top: 20px;
}

.register-link p {
  font-size: 14px;
}

.register-link a {
  color: #1e3a8a;
  text-decoration: none;
}

.register-link a:hover {
  text-decoration: underline;
}
</style>
