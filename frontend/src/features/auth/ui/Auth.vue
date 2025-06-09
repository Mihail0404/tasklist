<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";
import * as auth from "@/features/auth/model";

const schema = toTypedSchema(
  yup.object({
    login: yup.string().required(),
    password: yup.string().required(),
  })
);

const { errors, defineField, handleSubmit } = useForm({
  validationSchema: schema,
});

const [login, loginAttrs] = defineField("login");
const [password, passwordAttrs] = defineField("password");

function userSignIn(userdata: { login: string; password: string }) {
  auth.ApiAuth(userdata);
}
const onSubmit = handleSubmit((values) => {
  userSignIn(values);
  window.location.href = "/tasks";
});
</script>
<template>
  <div class="auth-form">
    <h2>Авторизация</h2>
    <form class="form" @submit="onSubmit">
      <label for="login">Логин</label>
      <input v-model="login" type="text" v-bind="loginAttrs" />
      <div class="errors">{{ errors.login }}</div>
      <label for="date">Пароль</label>
      <input v-model="password" type="password" v-bind="passwordAttrs" />
      <div class="errors">{{ errors.password }}</div>
      <button id="create-button" type="submit">Войти</button>
    </form>
  </div>
</template>
