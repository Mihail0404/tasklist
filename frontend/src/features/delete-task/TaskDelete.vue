<script setup lang="ts">
import * as taskEntity from "../../entities/task";

const sharedTasks = taskEntity.Model.Store.useSharedTasks().tasks;

defineProps<{
  name: string;
  description: string;
  date: Date;
}>();

function deleteTask(obj: taskEntity.Model.Types.TaskType) {
  // здесь апи удаления задачи
  let i = 0;
  for (const task of sharedTasks.value) {
    if (obj.name == task.name) {
      sharedTasks.value.splice(i, 1);
    }

    i++;
  }
}
</script>

<template>
  <button
    class="delete"
    @click="
      deleteTask({
        name: name,
        description: description,
        date: date,
      })
    "
  >
    Удалить
  </button>
</template>
