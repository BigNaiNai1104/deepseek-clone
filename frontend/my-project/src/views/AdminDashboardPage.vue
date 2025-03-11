<template>
  <div>
    <h1>Admin Dashboard</h1>
    <p>Welcome, Admin!</p>
    <h2>User Information</h2>
    <table v-if="users.length">
      <thead>
        <tr>
          <th>Username</th>
          <th>Email</th>
          <th>Registered Date</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(user, index) in users" :key="index">
          <td>{{ user.username }}</td>
          <td>{{ user.email }}</td>
          <td>{{ user.registered_date }}</td>
        </tr>
      </tbody>
    </table>
    <p v-else>No users found.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: "AdminDashboardPage",
  data() {
    return {
      users: []
    };
  },
  created() {
    this.fetchUsers();
  },
  methods: {
    async fetchUsers() {
      try {
        const token = localStorage.getItem("access_token");
        const response = await axios.get("http://localhost:8000/admin/users", {
          headers: {
            Authorization: `Bearer ${token}`
          }
        });
        this.users = response.data;  // 假设后端返回的是用户数组
      } catch (error) {
        console.error("Error fetching users:", error);
        alert("Failed to fetch user data.");
      }
    }
  }
};
</script>

<style scoped>
h1 {
  color: #42b983;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 20px;
}

table th,
table td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

table th {
  background-color: #f4f4f4;
}
</style>
