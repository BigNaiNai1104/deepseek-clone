import { createRouter, createWebHistory } from 'vue-router';

// 懒加载方式引入组件
const HomePage = () => import('../views/HomePage.vue');
const LoginPage = () => import('../views/LoginPage.vue');
const UserProfile = () => import('../views/UserProfile.vue');
const ChatPage = () => import('../views/ChatPage.vue');

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile,
    meta: { requiresAuth: true },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatPage,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

// 导航守卫：保护需要认证的路由
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('access_token')) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router;
