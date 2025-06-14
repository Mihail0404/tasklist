import { createSharedComposable } from "@vueuse/core";
import * as Types from "@/entities/task/model/types";
import { ref } from "vue";
import * as Api from "../api";

function useTasks() {
  const tasks = ref<Types.Task[]>([]);
  if (tasks.value.length === 0) {
    fetchAll();
  }

  async function fetchAll() {
    const userId = await Api.getUserData();
    tasks.value = await Api.getTasksByOwnerId(userId.id);
    console.log(tasks.value);
  }

  return { tasks, fetchAll };
}

const useSharedTasks = createSharedComposable(useTasks);

export { useSharedTasks };
