from sqlalchemy import BigInteger, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base

class Floor(Base):
    __tablename__ = "floor"

    id_floor: Mapped[int] = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    building_id: Mapped[int] = mapped_column(BigInteger, ForeignKey("building.id_building"), nullable=False)
