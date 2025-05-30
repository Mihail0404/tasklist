import { createWebHistory, createRouter } from "vue-router";

import RegisterPage from "./pages/RegisterPage.vue";
import AuthPage from "./pages/AuthPage.vue";
import BasePage from "./pages/BasePage.vue";
import TasksPage from "./pages/TasksPage.vue";

const routes = [
  {
    path: "",
    component: BasePage,
    children: [
      { path: "reg", component: RegisterPage },
      { path: "auth", component: AuthPage },
      { path: "tasks", component: TasksPage },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
