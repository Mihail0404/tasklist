import * as api from "../api";
import * as taskEntity from "@/entities/task";

const sharedTasks = taskEntity.Model.Store.useSharedTasks().tasks;

export default async function addTask(taskToCreate: {
  ownerId: number;
  name: string;
  description: string;
  completedAt: string;
  createdAt: string;
}) {
  const task = await api.createTask(taskToCreate);
  sharedTasks.value.push(task);
}
