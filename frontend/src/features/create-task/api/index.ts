import createClient from "openapi-fetch";
import type { paths } from "@/../rest-schema.d.ts";
import * as taskEntity from "@/entities/task";

const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});

const sharedTasks = taskEntity.Model.Store.useSharedTasks().tasks;

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
  completedAt: string;
  createdAt: string;
}) {
  const response = await client.POST("/api/tasks", {
    body: {
      ownerId: task.ownerId,
      name: task.name,
      description: task.description,
      complitedAt: task.completedAt,
      createdAt: task.createdAt,
    },
  });

  return normalizeTask(response.data!);
}
