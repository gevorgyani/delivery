import datetime
from fastapi import HTTPException
from pydantic import BaseModel, EmailStr, validator, constr
from typing import Optional, List
from pydantic import BaseModel
from app.crud.crud_user import user_crud


class Token(BaseModel):
    access_token: str
    token_type: str
    refresh_token: str


class BaseUser(BaseModel):
    id: int
    email: EmailStr

    # name: str

    class Config:
        orm_mode = True


class UpdateUser(BaseModel):
    id: Optional[int]
    email: Optional[str] = None
    # name: Optional[str] = None
    password: Optional[str] = None


class UpdateUserForOrg(BaseModel):
    email: Optional[EmailStr] = None
    # name: Optional[constr(min_length=1, max_length=50, regex=r'^[А-Яа-яЁё]+$')] = None
    password: Optional[str] = None

    @validator("password")
    def validate_password(cls, value):
        # Ваша валидация пароля здесь
        if value is None:
            raise ValueError("Пароль не может быть пустым.")
        if len(value) < 8:
            raise ValueError("Пароль должен содержать не менее 8 символов.")
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру.")
        if not any(char.isalpha() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну букву.")
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise ValueError("Пароль должен содержать хотя бы один специальный символ.")
        return value


class UpdateUserInDb(BaseModel):
    id: int
    email: Optional[str] = None
    # name: Optional[str] = None
    hashed_password: Optional[str] = None


class CreateAdminUser(BaseModel):
    email: EmailStr
    password: str


class LoginUser(BaseModel):
    email: EmailStr
    password: str


class CreateUserInDb(BaseModel):
    email: EmailStr

    hashed_password: str


class TokenData(BaseModel):
    email: str


class UpdatePassword(BaseModel):
    old_password: str
    new_password: str

    @validator("new_password")
    def validate_new_password(cls, value):
        # Ваша валидация пароля здесь
        if value is None:
            raise ValueError("Пароль не может быть пустым.")
        if len(value) < 8:
            raise ValueError("Пароль должен содержать не менее 8 символов.")
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру.")
        if not any(char.isalpha() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну букву.")
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise ValueError("Пароль должен содержать хотя бы один специальный символ.")
        return value


class PasswordGenerate(BaseModel):
    password: str


class UpdatePasswordAdmin(BaseModel):
    new_password: str

    @validator("new_password", pre=True)
    def validate_new_password(cls, value):
        # Ваша валидация пароля здесь
        if value is None:
            raise ValueError("Пароль не может быть пустым.")
        if len(value) < 8:
            raise ValueError("Пароль должен содержать не менее 8 символов.")
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру.")
        if not any(char.isalpha() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну букву.")
        if not any(char in '!@#$%^&*()_+' for char in value):
            raise ValueError("Пароль должен содержать хотя бы один специальный символ.")
        return value
