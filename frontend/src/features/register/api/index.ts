import createClient from "openapi-fetch";
import type { paths } from "../../../../rest-schema";

const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});

export default async function Reg(
  name: string,
  login: string,
  password: string
) {
  const { data, error } = await client.POST("/api/sign-up", {
    body: {
      name: name,
      login: login,
      password: password,
    },
  });
  let tasks: Types.ApiTaskType[] = await data;
  return tasks;
}
