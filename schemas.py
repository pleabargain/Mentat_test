from pydantic import BaseModel

class UserResponse(BaseModel):
    id: str
    name: str
    age: int
    favorite_pet: str

    class Config:
        orm_mode = True