import { client } from "@/shared/api";

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
  ownerId: number;
  name: string;
  description: string;
  completedAt: string | null;
  createdAt: string;
}) {
  const response = await client.POST("/api/tasks", {
    body: {
      ownerId: task.ownerId,
      name: task.name,
      description: task.description,
      completedAt: task.completedAt ? task.completedAt : null,
      createdAt: task.createdAt,
    },
  });

  return normalizeTask(response.data!);
}
