import re
from typing import ClassVar

from pydantic import BaseModel, EmailStr, Field, field_validator


class UserCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=50)
    surname: str = Field(..., min_length=3, max_length=50)
    mail: EmailStr
    password: str = Field(..., min_length=8, max_length=255)
    gender: str | None = None
    id_role: int

    VALID_GENDERS: ClassVar[set[str]] = {"homme", "femme", "non renseigne"}

    @field_validator("gender")
    @classmethod
    def validate_gender(cls, value: str | None) -> str | None:
        if value in (None, ""):
            return None
        if value not in cls.VALID_GENDERS:
            raise ValueError("Le genre selectionne n'est pas valide.")
        return value

    @field_validator("password")
    @classmethod
    def password_strength(cls, value: str) -> str:
        if (
            len(value) < 8
            or not any(char.isalpha() for char in value)
            or not any(char.isdigit() for char in value)
            or not any(char.islower() for char in value)
            or not any(char.isupper() for char in value)
            or not any(char in "!@#$%^&*()-_=+[]{}|;:,.<>?/" for char in value)
        ):
            raise ValueError(
                "Votre mot de passe doit contenir au moins 8 caracteres, "
                "avec une majuscule, un chiffre et un caractere special."
            )
        return value


class UserLogin(BaseModel):
    mail: EmailStr
    password: str = Field(..., min_length=8)
