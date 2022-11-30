from pydantic import BaseModel


class UserSchema(BaseModel):
    firstname: str
    lastname: str
    dad: str
    phone: str
    text: str

    class Config:
        orm_mode = True