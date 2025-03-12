<template>
  <div>
    <form @submit.prevent="login">
      <input v-model="username" placeholder="用户名" />
      <input v-model="password" type="password" placeholder="密码" />
      <button type="submit">登录</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      // 假设这里是登录逻辑
      const loginSuccess = true; // 模拟登录成功
      if (loginSuccess) {
        // 存储 token 信息
        localStorage.setItem('access_token', 'your-token-here');
        
        // 跳转到聊天页面
        this.$router.push({ name: 'chat' });
      } else {
        alert('登录失败');
      }
    },
  },
};
</script>
