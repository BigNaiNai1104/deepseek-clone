import { createRouter, createWebHistory } from 'vue-router';

// 懒加载组件
//const HomePage = () => import('../views/HomePage.vue');
const ChatPage = () => import('../views/ChatPage.vue');
const LoginPage = () => import('../views/LoginPage.vue');
const UserProfile = () => import('../views/UserProfile.vue');
const EditProfile = () => import('../views/EditProfile.vue');

const routes = [
  {
    path: '/',
    redirect: '/chat', // 访问根路径时跳转到聊天页面
  },
  {
    path: '/chat',
    name: 'chat',
    component: ChatPage,
    meta: { requiresAuth: true },
  },
  {
    path: '/login',
    name: 'login',
    component: LoginPage,
  },
  {
    path: '/profile',
    name: 'profile',
    component: UserProfile,
    meta: { requiresAuth: true },
  },
  {
    path: '/edit-profile',
    name: 'edit-profile',
    component: EditProfile,
    meta: { requiresAuth: true },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 路由守卫，确保用户登录后才能访问
router.beforeEach((to, from, next) => {
  if (to.meta.requiresAuth && !localStorage.getItem('access_token')) {
    next({ name: 'login' });
  } else {
    next();
  }
});

export default router;
