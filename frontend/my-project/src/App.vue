<template>
  <div>
    <nav>
      <router-link to="/">Home</router-link>
      <router-link v-if="!isAuthenticated" to="/login">Login</router-link>
      <router-link v-if="isAuthenticated" to="/dashboard">Dashboard</router-link>
      <button v-if="isAuthenticated" @click="logoutUser">Logout</button>
    </nav>
    <router-view />
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  computed: {
    ...mapGetters(["isAuthenticated", "getUser"]),
  },
  methods: {
    ...mapActions(["logout"]),
    logoutUser() {
      this.logout();
      this.$router.push("/login");
    },
  },
};
</script>
