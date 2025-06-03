import { client } from "@/shared/api";
import * as MiddleWare from "@/shared/api/middleware";

export type ApiTaskType = {
  id: number;
  name: string;
  description: string;
  ownerId: number;
  createdAt: Date;
  completedAt: string | null;
};

client.use(MiddleWare.ErrorMiddleware);

function normalizeTask(
  tasksToNormalize: {
    id: number;
    ownerId: number;
    name: string;
    description: string;
    completedAt: string | null;
    createdAt: string;
  }[]
) {
  const normalizedTasks: {
    id: number;
    ownerId: number;
    name: string;
    description: string;
    completedAt: Date | null;
    createdAt: Date;
  }[] = [];
  for (let el of tasksToNormalize) {
    const task = {
      ...el,
      completedAt: el.completedAt ? new Date(el.completedAt) : null,
      createdAt: new Date(el.createdAt),
    };
    normalizedTasks.push(task);
  }
  return normalizedTasks;
}

export default async function getTasksByOwnerId(ownerId: number) {
  const response = await client.GET("/api/tasks", {
    params: {
      query: { ownerId: ownerId },
    },
  });
  return normalizeTask(response.data!);
}
