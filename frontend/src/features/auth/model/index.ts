import * as api from "../api";

export async function ApiAuth(UserToSignIn: {
  login: string;
  password: string;
}) {
  await api.auth(UserToSignIn);
}
