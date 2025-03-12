<template>
    <div class="profile-container">
      <div class="profile-card">
        <h2>User Profile</h2>
        <div class="profile-info">
          <img class="profile-img" src="user-avatar.png" alt="User Avatar" />
          <div class="profile-details">
            <p><strong>Username:</strong> {{ user.username }}</p>
            <p><strong>Email:</strong> {{ user.email }}</p>
          </div>
        </div>
        <button @click="editProfile" class="btn">Edit Profile</button>
        <button @click="logout" class="btn logout-btn">Logout</button>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        user: {
          username: '',
          email: '',
        },
      };
    },
    created() {
      this.getUserProfile();
    },
    methods: {
      async getUserProfile() {
        try {
          const token = localStorage.getItem('access_token');
          if (!token) {
            this.$router.push({ name: 'login' });
            return;
          }
  
          const response = await axios.get('http://localhost:8000/profile', {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          });
  
          this.user = response.data;
        } catch (error) {
          console.error('Error fetching user profile:', error);
          this.$router.push({ name: 'login' });
        }
      },
      editProfile() {
        this.$router.push({ name: 'edit-profile' });
      },
      logout() {
        localStorage.removeItem('access_token');
        this.$router.push({ name: 'login' });
      },
    },
  };
  </script>
  
  <style scoped>
  .profile-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    background-color: #f4f4f4;
  }
  
  .profile-card {
    background-color: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 300px;
    text-align: center;
  }
  
  .profile-info {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 20px;
  }
  
  .profile-img {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    margin-bottom: 10px;
  }
  
  .profile-details p {
    font-size: 16px;
  }
  
  .btn {
    width: 100%;
    padding: 10px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .logout-btn {
    background-color: #f44336;
  }
  
  .btn:hover {
    background-color: #45a049;
  }
  
  .logout-btn:hover {
    background-color: #e53935;
  }
  </style>
  