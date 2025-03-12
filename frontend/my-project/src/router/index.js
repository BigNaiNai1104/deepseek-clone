import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/HomePageAlternative.vue';
import UserProfile from '../views/UserProfile.vue';
import LoginPage from '../views/LoginPage.vue'; // 引入 LoginPage
import EditProfile from '../views/EditProfile.vue'; // 引入 EditProfile 组件

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile,
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/edit-profile', // 新的路由路径
    name: 'edit-profile',  // 路由的名称
    component: EditProfile, // 绑定到 EditProfile 组件
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
