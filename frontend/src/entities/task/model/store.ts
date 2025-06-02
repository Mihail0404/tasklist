import { createSharedComposable } from "@vueuse/core";
import * as Types from "@/entities/task/model/types";
import { ref } from "vue";

function useTasks() {
  const tasks = ref<Types.Task[]>([]);
  fetch();

  async function fetch() {
    // tasks.value = await Api.get_task(2);
  }

  return { tasks, fetch };
}

const useSharedTasks = createSharedComposable(useTasks);

export { useSharedTasks };
