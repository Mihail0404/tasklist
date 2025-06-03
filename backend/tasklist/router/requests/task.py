import pydantic
import pydantic.alias_generators

class Task(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(alias_generator=pydantic.alias_generators.to_camel)
    owner_id: int # = pydantic.Field(serialization_alias='ownerId')
    name: str
    description: str
    completed_at: str | None# = pydantic.Field(serialization_alias='completedAt')
    created_at: str #= pydantic.Field(serialization_alias='createdAt')
