<script setup lang="ts">
import TaskDelete from "@/features/delete-task/TaskDelete.vue";

defineProps<{
  title: string;
  description: string;
  date: Date;
}>();
</script>
<template>
  <p class="task-title">
    <strong>{{ title }} </strong>
  </p>
  <p>{{ description }}</p>
  <p>
    {{
      date.getDate() + "/" + (date.getMonth() + 1) + "/" + date.getFullYear()
    }}
  </p>
  <TaskDelete :name="title" :description="description" :date="date" />
</template>
