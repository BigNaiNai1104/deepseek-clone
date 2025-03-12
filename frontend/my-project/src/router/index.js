import { createRouter, createWebHistory } from 'vue-router';
import LoginPage from '../views/LoginPage.vue';
import RegisterPage from '../views/RegisterPage.vue';
import UserProfile from '../views/UserProfile.vue';  // 引入 UserProfile.vue

const routes = [
  {
    path: '/',
    redirect: '/login',  // 让根路径自动跳转到 /login
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterPage,
  },
  {
    path: '/profile',  // 用户资料页面路径
    name: 'profile',
    component: UserProfile,  // 使用 UserProfile 组件
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
