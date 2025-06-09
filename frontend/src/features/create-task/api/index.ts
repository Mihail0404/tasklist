import { client } from "@/shared/api";
import * as Api from "@/entities/task/api";

function normalizeTask(taskToNormalize: {
  id: number;
  ownerId: number;
  name: string;
  description: string;
  completedAt: string | null;
  createdAt: string;
}) {
  return {
    ...taskToNormalize,
    completedAt: taskToNormalize.completedAt
      ? new Date(taskToNormalize.completedAt)
      : null,
    createdAt: new Date(taskToNormalize.createdAt),
  };
}

export async function createTask(task: {
  name: string;
  description: string;
  completedAt: string | null;
}) {
  const response = await client.POST("/api/tasks", {
    body: {
      ownerId: (await Api.getUserData()).id,
      name: task.name,
      description: task.description,
      completedAt: task.completedAt ? task.completedAt : null,
    },
  });

  return normalizeTask(response.data!);
}
