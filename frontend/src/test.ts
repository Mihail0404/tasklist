async function test() {
  const response = await fetch("/api/sign-in", {
    method: "POST",
    headers: {
      "Content-Type": "application/json;charset=utf-8",
    },
    body: '{"login": "admin","password": "12345678"}',
  });
  return response.json();
}

console.log(test());
