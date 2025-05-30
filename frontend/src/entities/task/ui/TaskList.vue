<script setup lang="ts">
import TaskCard from "./TaskCard.vue";

import * as Model from "../model";

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
