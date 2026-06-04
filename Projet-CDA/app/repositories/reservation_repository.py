from datetime import date, time
from app.database.engine import SessionLocal
from app.models.reservation import Reservation

class ReservationRepository:
    def get_all(self) -> list[Reservation]:
        with SessionLocal() as session:
            return session.query(Reservation).all()
    
    def get_by_id(self, reservation_id: int) -> Reservation | None:
        with SessionLocal() as session:
            return session.query(Reservation).filter(Reservation.id_reservation == reservation_id).first()
    
    def get_by_classroom(self, classroom_id: int) -> list[Reservation]:
        with SessionLocal() as session:
            return session.query(Reservation).filter(Reservation.id_classroom == classroom_id).all()
    
    def get_by_user(self, user_id: int) -> list[Reservation]:
        with SessionLocal() as session:
            return session.query(Reservation).filter(Reservation.id_user == user_id).all()
    
    def get_by_date(self, date_reservation: date) -> list[Reservation]:
        with SessionLocal() as session:
            return session.query(Reservation).filter(Reservation.date_reservation == date_reservation).all()
    
    def get_by_classroom_and_date(self, classroom_id: int, date_reservation: date) -> list[Reservation]:
        with SessionLocal() as session:
            return session.query(Reservation).filter(
                Reservation.id_classroom == classroom_id,
                Reservation.date_reservation == date_reservation
            ).all()
    
    def add(self, reservation_data: dict):
        with SessionLocal() as session:
            reservation = Reservation(**reservation_data)
            session.add(reservation)
            session.commit()
            return reservation
    
    def update(self, reservation_id: int, reservation_data: dict):
        with SessionLocal() as session:
            reservation = session.query(Reservation).filter(Reservation.id_reservation == reservation_id).first()
            if reservation:
                for key, value in reservation_data.items():
                    setattr(reservation, key, value)
                session.commit()
            return reservation
    
    def delete(self, reservation_id: int):
        with SessionLocal() as session:
            reservation = session.query(Reservation).filter(Reservation.id_reservation == reservation_id).first()
            if reservation:
                session.delete(reservation)
                session.commit()
