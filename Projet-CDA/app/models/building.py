from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Building(Base):
    __tablename__ = "building"

    id_building: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False, unique=True)
    id_address: Mapped[int] = mapped_column(BigInteger, nullable=True)
