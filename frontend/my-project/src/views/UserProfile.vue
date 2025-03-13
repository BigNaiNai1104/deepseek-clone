<template>
  <div class="profile-container">
    <h2>User Profile</h2>
    <p><strong>Username:</strong> {{ username }}</p>
    <p><strong>Email:</strong> {{ email }}</p>
    <button class="edit-btn" @click="goToEditProfile">修改个人资料</button>
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
        if (!token) {
          this.$router.push({ name: "login" });
          return;
        }
        const response = await axios.get("http://localhost:8000/profile", {
          headers: { Authorization: `Bearer ${token}` },
        });
        this.username = response.data.username;
        this.email = response.data.email;
      } catch (error) {
        console.error("Error fetching profile:", error);
      }
    },
    goToEditProfile() {
      this.$router.push({ name: "edit-profile" });
    },
  },
};
</script>

<style scoped>
.profile-container {
  padding: 20px;
}

.edit-btn {
  padding: 10px;
  font-size: 14px;
  color: white;
  background-color: blue;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

.edit-btn:hover {
  opacity: 0.8;
}
</style>
