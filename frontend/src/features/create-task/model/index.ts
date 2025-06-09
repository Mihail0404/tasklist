import * as api from "../api";
import * as taskEntity from "@/entities/task";

const sharedTasks = taskEntity.Model.Store.useSharedTasks().tasks;

export default async function addTask(taskToCreate: {
  name: string;
  description: string;
  completedAt: string | null;
}) {
  const task = await api.createTask(taskToCreate);
  sharedTasks.value.push(task);
}
