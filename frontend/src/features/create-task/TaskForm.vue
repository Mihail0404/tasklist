<script setup lang="ts">
import { useForm } from "vee-validate";
import { toTypedSchema } from "@vee-validate/yup";
import * as yup from "yup";

import * as taskEntity from "../../entities/task";
import getTasksByOwnerId from "../../entities/task/api/index";

console.log(getTasksByOwnerId(2));

const sharedTasks = taskEntity.Model.Store.useSharedTasks().tasks;

const schema = toTypedSchema(
  yup.object({
    title: yup.string().required(),
    description: yup.string().required(),
    date: yup.date().required(),
  })
);

const { errors, defineField, handleSubmit } = useForm({
  validationSchema: schema,
});

const [name, nameAttrs] = defineField("title");
const [description, descriptionAttrs] = defineField("description");
const [date, dateAttrs] = defineField("date");

function addTask(obj: taskEntity.Model.Types.TaskType) {
  sharedTasks.value.push(obj);
  // здесь апи добавления задачи
}

const onSubmit = handleSubmit((values) => {
  addTask(values);
});
</script>
<template>
  <div class="wrapper">
    <h2>Задачи</h2>
    <form class="form" @submit="onSubmit">
      <label for="title">Название задачи</label>
      <input v-model="name" type="text" v-bind="nameAttrs" />
      <div class="errors">{{ errors.title }}</div>
      <label for="description">Описание задачи</label>
      <input v-model="description" type="text" v-bind="descriptionAttrs" />
      <div class="errors">{{ errors.description }}</div>
      <label for="date">Дата создания</label>
      <input v-model="date" type="date" v-bind="dateAttrs" />
      <div class="errors">{{ errors.date }}</div>
      <button id="create-button" type="submit">Создать</button>
    </form>
  </div>
</template>
