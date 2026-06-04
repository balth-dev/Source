from datetime import datetime, date, time
from sqlalchemy.orm import mapped_column
from sqlalchemy import BigInteger, Date, Time, ForeignKey, String
from app.database.base import Base

class Reservation(Base):
    __tablename__ = "reservation"

    id_reservation = mapped_column(BigInteger, primary_key=True, autoincrement=True)
    date_reservation = mapped_column(Date, nullable=False)
    start_time = mapped_column(Time, nullable=False)
    end_time = mapped_column(Time, nullable=False)
    status = mapped_column(String(50), nullable=True)
    id_classroom = mapped_column(BigInteger, ForeignKey("Classroom.id_classroom"), nullable=False)
    id_user = mapped_column(BigInteger, ForeignKey("user.id_user"), nullable=False)
