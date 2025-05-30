<script setup lang="ts"></script>
<template>
  <nav>
    <RouterLink class="header" to="/auth">Авторизация</RouterLink>
    <RouterLink class="header" to="/reg">Регистрация</RouterLink>
    <RouterLink class="header" to="/tasks">Задачи</RouterLink>
  </nav>
  <RouterView />
</template>
