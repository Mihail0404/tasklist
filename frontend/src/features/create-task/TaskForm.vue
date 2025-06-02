<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";
import addTask from "@/features/create-task/model";

const schema = toTypedSchema(
  yup.object({
    title: yup.string().required(),
    description: yup.string().required(),
    owner_id: yup.number().required(),
    created_at: yup.date().required(),
    completed_at: yup.date().required(),
  })
);

const { errors, defineField, handleSubmit } = useForm({
  validationSchema: schema,
});

const [title, nameAttrs] = defineField("title");
const [description, descriptionAttrs] = defineField("description");
const [owner_id, owneridAttrs] = defineField("owner_id");
const [created_at, createdatAttrs] = defineField("created_at");
const [completed_at, completedatAttrs] = defineField("completed_at");

const onSubmit = handleSubmit((values) => {
  addTask(values);
});
</script>
<template>
  <div class="wrapper">
    <h2>Задачи</h2>
    <form class="form" @submit="onSubmit">
      <label for="title">Название задачи</label>
      <input v-model="title" type="text" v-bind="nameAttrs" />
      <div class="errors">{{ errors.title }}</div>
      <label for="description">Описание задачи</label>
      <input v-model="description" type="text" v-bind="descriptionAttrs" />
      <div class="errors">{{ errors.description }}</div>
      <label for="owner_id">owner_id</label>
      <input v-model="owner_id" type="text" v-bind="owneridAttrs" />
      <div class="errors">{{ errors.owner_id }}</div>
      <label for="date">Дата создания</label>
      <input v-model="created_at" type="date" v-bind="createdatAttrs" />
      <div class="errors">{{ errors.created_at }}</div>
      <label for="date">Дата выполнения</label>
      <input v-model="completed_at" type="date" v-bind="completedatAttrs" />
      <div class="errors">{{ errors.completed_at }}</div>
      <button id="create-button" type="submit">Создать</button>
    </form>
  </div>
</template>
