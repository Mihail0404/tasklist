<script setup lang="ts">
import TaskCard from "@/entities/task/ui/TaskCard.vue";

import * as Model from "@/entities/task/model";
import { ref } from "vue";
import getTasksByOwnerId from "@/entities/task/api";

const tasksFromApi = ref<
  {
    id: number;
    ownerId: number;
    name: string;
    description: string;
    completedAt: string | null;
    createdAt: string;
  }[]
>([]);

async function fetchAll() {
  tasks.value = await getTasksByOwnerId(2);
  console.log(tasks.value);
}

fetchAll();

const { tasks } = Model.Store.useSharedTasks();
</script>
<template>
  <div class="task-cards">
    <div v-for="task in tasks" :key="task.name" class="task">
      <TaskCard
        :title="task.name"
        :description="task.description"
        :date="task.createdAt"
      />
    </div>
  </div>
</template>
