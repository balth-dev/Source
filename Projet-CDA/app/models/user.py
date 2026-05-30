import enum
from sqlalchemy.orm import mapped_column, DeclarativeBase
from sqlalchemy import Enum, ForeignKey

from app.database.base import Base
from sqlalchemy import Column, Integer, String, BigInteger

class GenderEnum(enum.Enum):
    male = "homme"
    female = "femme"
    other = "non renseigné"

class User(Base):
    __tablename__ = "user"

    id_user = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name = mapped_column(String(50), nullable=False)
    first_name = mapped_column(String(50), nullable=False)
    email = mapped_column(String(100), unique=True, nullable=False)
    password = mapped_column(String(200), nullable=False)
    gender = mapped_column(String(20), nullable=True)
    id_role = mapped_column(BigInteger, ForeignKey("role.id_role"), nullable=False)
    
    
#user_create.password = hashpw(user_create.password)