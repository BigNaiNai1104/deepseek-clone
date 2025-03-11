import { createStore } from "vuex";

const store = createStore({
  state() {
    return {
      user: null // 用来存储用户登录信息
    };
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
    logout(state) {
      state.user = null;
    }
  },
  actions: {
    login({ commit }, user) {
      // 这里可以添加实际的登录逻辑，比如请求后端接口
      commit("setUser", user);
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
