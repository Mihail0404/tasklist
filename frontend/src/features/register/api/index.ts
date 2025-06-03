import { client } from "@/shared/api";

export async function reg(user: {
  name: string;
  login: string;
  password: string;
}) {
  const response = await client.POST("/api/sign-up", {
    body: {
      name: user.name,
      login: user.login,
      password: user.password,
    },
  });
  return response.data!;
}
