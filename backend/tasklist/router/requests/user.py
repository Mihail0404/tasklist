import pydantic

class User(pydantic.BaseModel):
    name: str
    login: str
    password: str

class Auth(pydantic.BaseModel):
    login: str
    password: str