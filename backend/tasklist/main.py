from fastapi import FastAPI
from tasklist import router
import sqlalchemy.ext.asyncio as sa_asynio
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://localhost:5174",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/")
def server_status():
    return {"status": "Works"}

from sys import path

print(path)

app.include_router(router.routes.task_router)
app.include_router(router.routes.user_router)
