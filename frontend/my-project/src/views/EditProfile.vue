<template>
    <div class="edit-profile-container">
      <h2>Edit Profile</h2>
      <form @submit.prevent="saveProfile">
        <div>
          <label for="username">Username</label>
          <input type="text" v-model="username" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" v-model="email" required />
        </div>
        <button type="submit" class="btn">Save</button>
      </form>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    data() {
      return {
        username: "",
        email: "",
      };
    },
    created() {
      this.getUserProfile();
    },
    methods: {
      async getUserProfile() {
        try {
          const token = localStorage.getItem("access_token");
          const response = await axios.get("http://localhost:8000/profile", {
            headers: { Authorization: `Bearer ${token}` },
          });
          this.username = response.data.username;
          this.email = response.data.email;
        } catch (error) {
          console.error("Error fetching profile:", error);
        }
      },
      async saveProfile() {
        try {
          const token = localStorage.getItem("access_token");
          await axios.put(
            "http://localhost:8000/profile",
            { username: this.username, email: this.email },
            { headers: { Authorization: `Bearer ${token}` } }
          );
          this.$router.push({ name: "profile" });
        } catch (error) {
          console.error("Error saving profile:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .edit-profile-container {
    padding: 20px;
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    width: 300px;
    margin: 0 auto;
  }
  
  h2 {
    text-align: center;
    margin-bottom: 20px;
  }
  
  form {
    display: flex;
    flex-direction: column;
  }
  
  form div {
    margin-bottom: 15px;
  }
  
  label {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 5px;
  }
  
  input {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  button {
    width: 100%;
    padding: 10px;
    font-size: 16px;
    background-color: #4CAF50;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    margin-top: 10px;
  }
  
  button:hover {
    opacity: 0.8;
  }
  </style>
  