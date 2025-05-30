import * as Types from "../model/types";

import createClient from "openapi-fetch";
import type { paths } from "../../../../rest-schema";

const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});

export type ApiTaskType = {
  id: number;
  name: string;
  description: string;
  ownerId: number;
  createdAt: string;
  completedAt: string | null;
};

export default async function getTasksByOwnerId(ownerId: number) {
  const { data, error } = await client.GET("/api/tasks", {
    params: {
      query: { ownerId: ownerId },
    },
  });
  let tasks: Types.ApiTaskType[] = await data;
  return tasks;
}
