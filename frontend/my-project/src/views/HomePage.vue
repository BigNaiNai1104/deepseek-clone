<template>
  <div>
    <h1>Welcome to DeepSeek Clone</h1>
    <div v-if="isAuthenticated">
      <p>Welcome, {{ user.username }}!</p>
      <button @click="logout">Logout</button>
    </div>
    <div v-else>
      <p>Please log in to continue.</p>
      <router-link to="/login">Login</router-link>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "HomePage",
  computed: {
    ...mapGetters(["isAuthenticated", "getUser"])
  },
  methods: {
    ...mapActions(["logout"]),
  }
};
</script>

<style scoped>
h1 {
  color: #42b983;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  background-color: #42b983;
  color: white;
  border: none;
  cursor: pointer;
}

a {
  text-decoration: none;
  color: #42b983;
}
</style>
