<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";

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

function userLogin(obj) {
  // здесь апи атворизации
}
const onSubmit = handleSubmit((values) => {
  userLogin(values);
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
      <input v-model="password" type="text" v-bind="passwordAttrs" />
      <div class="errors">{{ errors.password }}</div>
      <button id="create-button" type="submit">Войти</button>
    </form>
  </div>
</template>
