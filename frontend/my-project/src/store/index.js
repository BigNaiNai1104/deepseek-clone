import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      user: JSON.parse(localStorage.getItem("user")) || null // 如果本地有用户数据就直接加载
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    logout(state) {
      state.user = null;
      localStorage.removeItem("access_token"); // 清除本地存储的token
      localStorage.removeItem("user"); // 清除用户数据
    }
  },
  actions: {
    login({ commit }, user) {
      commit("setUser", user);
      localStorage.setItem("user", JSON.stringify(user)); // 存储用户数据
    },
    logout({ commit }) {
      commit("logout");
    }
  },
  getters: {
    isAuthenticated(state) {
      return !!state.user;
    },
    getUser(state) {
      return state.user;
    }
  }
});

export default store;
