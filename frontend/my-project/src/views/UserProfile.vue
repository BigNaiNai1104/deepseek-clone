<template>
    <div class="profile-container">
      <h2>User Profile</h2>
      <div class="profile-info">
        <p><strong>Username:</strong> {{ profile.username }}</p>
        <p><strong>Email:</strong> {{ profile.email }}</p>
      </div>
      <button @click="editProfile" class="btn">Edit Profile</button>
    </div>
  </template>
  
  <script>
  import axios from 'axios'; // 导入 axios
  
  export default {
    data() {
      return {
        profile: {},
      };
    },
    async created() {
      const token = localStorage.getItem('access_token');
      try {
        const response = await axios.get('http://localhost:8000/profile', {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.profile = response.data;
      } catch (error) {
        console.error('Failed to fetch user profile:', error);
      }
    },
    methods: {
      editProfile() {
        // Navigate to edit profile page
        this.$router.push({ name: 'edit-profile' });
      },
    },
  };
  </script>
  
  <style scoped>
  .profile-container {
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    max-width: 500px;
    margin: 20px auto;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  .profile-info {
    margin-bottom: 20px;
  }
  
  strong {
    color: #333;
  }
  
  .btn {
    display: block;
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
  </style>
  