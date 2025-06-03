import { client } from "@/shared/api";

export default async function deleteTaskById(id: number) {
  const { data, error } = await client.DELETE("/api/tasks/{id}", {
    params: {
      path: { id: id },
    },
  });
  return data;
}
