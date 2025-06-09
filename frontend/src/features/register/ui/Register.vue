<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";
import * as register from "@/features/register/model";

const schema = toTypedSchema(
  yup.object({
    name: yup.string().required(),
    login: yup.string().required(),
    password: yup.string().required(),
  })
);

const { errors, defineField, handleSubmit } = useForm({
  validationSchema: schema,
});

const [name, nameAttrs] = defineField("name");
const [login, loginAttrs] = defineField("login");
const [password, passwordAttrs] = defineField("password");

function addUser(user: { name: string; login: string; password: string }) {
  register.ApiAddUser(user);
}
const onSubmit = handleSubmit((values) => {
  addUser(values);
  window.location.href = "/auth";
});
</script>
<template>
  <div class="register-form">
    <h2>Регистрация</h2>
    <form class="form" @submit="onSubmit">
      <label for="name">Имя</label>
      <input v-model="name" type="text" v-bind="nameAttrs" />
      <div class="errors">{{ errors.name }}</div>
      <label for="login">Логин</label>
      <input v-model="login" type="text" v-bind="loginAttrs" />
      <div class="errors">{{ errors.login }}</div>
      <label for="date">Пароль</label>
      <input v-model="password" type="password" v-bind="passwordAttrs" />
      <div class="errors">{{ errors.password }}</div>
      <button id="create-button" type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>
