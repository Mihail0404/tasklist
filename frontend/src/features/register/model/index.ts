import * as api from "../api";

export async function ApiAddUser(UserToCreate: {
  name: string;
  login: string;
  password: string;
}) {
  await api.reg(UserToCreate);
}
