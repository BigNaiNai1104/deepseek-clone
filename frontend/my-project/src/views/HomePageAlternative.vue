<template>
  <div class="home-container">
    <h1>Welcome to DeepSeek Clone</h1>
    <p>This is your personalized homepage after login!</p>
    <router-link to="/profile" class="btn">Go to Profile</router-link>
  </div>
</template>

<script>
export default {
  name: 'HomePageAlternative',
};
</script>

<style scoped>
.home-container {
  padding: 40px;
  text-align: center;
  background: linear-gradient(to right, #6a11cb, #2575fc); /* 背景渐变 */
  color: white;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}

h1 {
  font-size: 3rem; /* 增加标题的字体大小 */
  margin-bottom: 20px;
  font-weight: bold;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3); /* 增加标题阴影 */
}

p {
  font-size: 1.5rem;
  margin-bottom: 30px;
}

.btn {
  padding: 15px 30px;
  font-size: 18px;
  background-color: #4CAF50;
  color: white;
  text-decoration: none;
  border-radius: 4px;
  display: inline-block;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 增加按钮阴影 */
  transition: all 0.3s ease; /* 按钮动画 */
}

.btn:hover {
  background-color: #45a049;
  transform: translateY(-2px); /* 鼠标悬浮时按钮上升 */
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.2); /* 鼠标悬浮时按钮阴影变大 */
}
</style>
