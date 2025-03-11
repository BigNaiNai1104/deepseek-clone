import { createRouter, createWebHistory } from 'vue-router'; // 确保使用 Vue Router 4.x 的方式

import HomePage from '@/views/HomePage.vue'; // 引入组件
import LoginPage from '@/views/LoginPage.vue';
import RegisterPage from '@/views/RegisterPage.vue';
import AdminDashboard from '@/views/AdminDashboardPage.vue';

const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/login',
    name: 'LoginPage',
    component: LoginPage,
  },
  {
    path: '/register',
    name: 'RegisterPage',
    component: RegisterPage,
  },
  {
    path: '/admin',
    name: 'AdminDashboard',
    component: AdminDashboard,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
