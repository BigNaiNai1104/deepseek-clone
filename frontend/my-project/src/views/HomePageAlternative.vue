<template>
    <div class="home-container">
      <h1>Welcome to DeepSeek Clone</h1>
      <p>This is your personalized homepage after login!</p>
      <router-link to="/profile" class="btn">Go to Profile</router-link>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomePageAlternative',  // 更改为不同的多词名称
  };
  </script>
  
  <style scoped>
  .home-container {
    padding: 40px;
    text-align: center;
  }
  
  h1 {
    font-size: 2rem;
    margin-bottom: 20px;
  }
  
  p {
    font-size: 1.2rem;
    margin-bottom: 30px;
  }
  
  .btn {
    padding: 10px 20px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    display: inline-block;
  }
  
  .btn:hover {
    background-color: #45a049;
  }
  </style>
  