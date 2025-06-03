<script setup lang="ts"></script>
<template>
  <nav>
    <RouterLink class="header" to="/auth">Авторизация</RouterLink>
    <RouterLink class="header" to="/reg">Регистрация</RouterLink>
    <RouterLink class="header" to="/tasks">Задачи</RouterLink>
  </nav>
  <RouterView />
</template>
<style>
.header {
  color: #fff;
  padding: 0 10px;
  text-decoration: none;
}

nav {
  background-color: #3b3b3b;
  padding: 20px;
  border-radius: 10px;
}
</style>
