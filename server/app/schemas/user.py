from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class Userlogin(BaseModel):
    email: EmailStr
    password: str

class UserInDB(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
        # orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str
