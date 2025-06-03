<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";
import addTask from "@/features/create-task/model";

const schema = toTypedSchema(
  yup.object({
    name: yup.string().required(),
    description: yup.string().required(),
    ownerId: yup.number().required(),
    createdAt: yup.date().required(),
    completedAt: yup.date(),
  })
);

const { errors, defineField, handleSubmit } = useForm({
  validationSchema: schema,
});

const [name, nameAttrs] = defineField("name");
const [description, descriptionAttrs] = defineField("description");
const [ownerId, owneridAttrs] = defineField("ownerId");
const [createdAt, createdatAttrs] = defineField("createdAt");
const [completedAt, completedatAttrs] = defineField("completedAt");

const onSubmit = handleSubmit((values) => {
  addTask({
    ...values,
    completedAt: values.completedAt
      ? values.completedAt.toLocaleDateString("en-US")
      : null,
    createdAt: values.createdAt.toLocaleDateString("en-US"),
  });
});
</script>
<template>
  <div class="wrapper">
    <h2>Задачи</h2>
    <form class="form" @submit="onSubmit">
      <label for="title">Название задачи</label>
      <input v-model="name" type="text" v-bind="nameAttrs" />
      <div class="errors">{{ errors.name }}</div>
      <label for="description">Описание задачи</label>
      <input v-model="description" type="text" v-bind="descriptionAttrs" />
      <div class="errors">{{ errors.description }}</div>
      <label for="owner_id">owner_id</label>
      <input v-model="ownerId" type="text" v-bind="owneridAttrs" />
      <div class="errors">{{ errors.ownerId }}</div>
      <label for="date">Дата создания</label>
      <input v-model="createdAt" type="date" v-bind="createdatAttrs" />
      <div class="errors">{{ errors.createdAt }}</div>
      <label for="date">Дата выполнения</label>
      <input v-model="completedAt" type="date" v-bind="completedatAttrs" />
      <div class="errors">{{ errors.completedAt }}</div>
      <button id="create-button" type="submit">Создать</button>
    </form>
  </div>
</template>
<style>
input {
  font-size: 20px;
  margin: 10px 0;
  display: block;
  width: 98%;
  background-color: #ffffff;
  border: none;
  border-radius: 3px;
  padding: 5px;
  outline: none;
}

.form {
  border-radius: 6px;
  border: 1px solid #000000;
  background-color: #3b3b3b;
  width: 350px;
  padding: 10px;
  margin: 10px 0;
  color: #fff;
  text-align: center;
}

.errors {
  color: rgb(255, 174, 0);
  margin: 10px 0;
}
</style>
