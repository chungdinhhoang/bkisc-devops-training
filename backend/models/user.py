
from pydantic import BaseModel

class UserModel(BaseModel):
    name: str
    username: str
    email: str
    hashedPassword: str

