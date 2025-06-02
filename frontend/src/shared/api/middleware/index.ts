export const ErrorMiddleware = {
  async onResponse({ response: Response }) {
    if (!response.ok) {
      const error = await response.json();

      throw error;
    }

    return undefined;
  },
};
