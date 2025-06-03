import type { Middleware } from "openapi-fetch";

export const ErrorMiddleware: Middleware = {
  async onResponse({ response }) {
    if (!response.ok) {
      const error = await response.json();

      throw error;
    }

    return undefined;
  },
};
