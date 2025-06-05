import { client } from "@/shared/api";

export async function deleteTaskById(id: number) {
  const response = await client.DELETE("/api/tasks/{id}", {
    params: {
      path: { id: id },
    },
  });
  
  return response.data!;
}
