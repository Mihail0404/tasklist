import { createSharedComposable } from "@vueuse/core";
import * as Types from "./types";
import { ref } from "vue";
import * as Api from "../api";

function useTasks() {
  const tasks = ref<Types.ApiTaskType[]>([]);
  fetch();

  async function fetch() {
    // tasks.value = await Api.get_task(2);
  }

  return { tasks, fetch };
}

const useSharedTasks = createSharedComposable(useTasks);

export { useSharedTasks };
