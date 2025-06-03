import createClient from "openapi-fetch";
import type { paths } from "../../../rest-schema";

export const client = createClient<paths>({
  baseUrl: "http://tasklist.localhost.com/",
});
