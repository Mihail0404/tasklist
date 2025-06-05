<script setup lang="ts">
import TaskCard from "@/entities/task/ui/TaskCard.vue";
import * as Model from "@/entities/task/model";

const { tasks } = Model.Store.useSharedTasks();
</script>
<template>
  <div class="task-cards">
    <div v-for="task in tasks" :key="task.name" class="task">
      <TaskCard
        :id="task.id"
        :title="task.name"
        :description="task.description"
        :date="task.createdAt"
      />
    </div>
  </div>
</template>
<style>
.task {
  padding: 10px;
  border: 1px solid black;
  border-radius: 6px;
  background-color: #c7c7c7;
  height: auto;
}
.task-cards {
  display: flex;
  flex-direction: row;
  gap: 15px;
}
</style>
