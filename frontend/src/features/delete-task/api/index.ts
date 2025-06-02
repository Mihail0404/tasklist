import createClient from "openapi-fetch";
import type { paths } from "@/../rest-schema";

const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});

export default async function deleteTaskById(id: number) {
  const { data, error } = await client.DELETE("/api/tasks/{id}", {
    params: {
      path: { id: id },
    },
  });
  return data;
}
