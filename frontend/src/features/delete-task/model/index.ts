import * as api from "../api";
import * as taskEntity from "@/entities/task";

export function deleteTask(id: number) {
  const { fetchAll }= taskEntity.Model.Store.useSharedTasks();
  api.deleteTaskById(id).then(fetchAll);
}
