<script setup lang="ts">
import TaskDelete from "@/features/delete-task/TaskDelete.vue";

defineProps<{
  title: string;
  description: string;
  date: Date;
}>();
</script>
<template>
  <div class="task-card">
    <p class="task-card__title">
      {{ title }}
    </p>
    <p class="task-card__description">{{ description }}</p>
    <p>
      {{
        date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear()
      }}
    </p>
    <TaskDelete :name="title" :description="description" :date="date" />
  </div>
</template>
<style>
.task-card__title {
  font-size: 36px;
  margin: 0;
  font-weight: bold;
}
</style>
