import { client } from "@/shared/api";

export async function auth(userdata: { login: string; password: string }) {
  const response = await client.POST("/api/sign-in", {
    body: {
      login: userdata.login,
      password: userdata.password,
    },
  });
  localStorage.setItem("login", response.data!.login);
  return response.data!;
}
