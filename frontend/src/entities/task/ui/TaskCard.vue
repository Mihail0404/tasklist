<script setup lang="ts">
import TaskDelete from "@/features/delete-task/TaskDelete.vue";

defineProps<{
  id: number;
  title: string;
  description: string;
  date: Date;
}>();
</script>
<template>
  <div class="task-card">
    <div class="task-card__title">
      {{ title }}
    </div>
    <div class="task-card__description">{{ description }}</div>
    <div class="task-card__create-date">
      Дата создания:
      {{
        date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear()
      }}
    </div>
    <TaskDelete :id="id" />
  </div>
</template>
<style>
.task-card__title {
  font-size: 36px;
  margin: 0;
  font-weight: bold;
}
</style>
