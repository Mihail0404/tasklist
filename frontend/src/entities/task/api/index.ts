import createClient from "openapi-fetch";
import type { paths } from "@/../rest-schema";
import * as MiddleWare from "@/shared/api/middleware";

const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});

export type ApiTaskType = {
  id: number;
  name: string;
  description: string;
  ownerId: number;
  createdAt: Date;
  completedAt: string | null;
};

client.use(MiddleWare.ErrorMiddleware);

export default async function getTasksByOwnerId(ownerId: number) {
  const response = await client.GET("/api/tasks", {
    params: {
      query: { ownerId: ownerId },
    },
  });
  return response.data!;
}
