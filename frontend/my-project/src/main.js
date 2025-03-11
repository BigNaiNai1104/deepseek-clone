import { createApp } from "vue";
import App from "./App.vue";
import store from "./store"; // 引入 Vuex store
import router from "./router"; // 引入 Vue Router

const app = createApp(App);

// 使用 Vuex 和 Vue Router
app.use(store); // 使用 Vuex
app.use(router); // 使用 Vue Router

app.mount("#app");
