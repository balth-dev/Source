from app.database.engine import SessionLocal
from app.models.classroom import Classroom

class ClassroomRepository:
    def get_all(self) -> list[Classroom]:
        with SessionLocal() as session:
            return session.query(Classroom).all()
    
    def get_by_id(self, classroom_id: int) -> Classroom | None:
        with SessionLocal() as session:
            return session.query(Classroom).filter(Classroom.id_classroom == classroom_id).first()
    
    def get_by_name(self, name: str) -> Classroom | None:
        with SessionLocal() as session:
            return session.query(Classroom).filter(Classroom.name == name).first()
    
    def add(self, classroom_data: dict):
        with SessionLocal() as session:
            classroom = Classroom(**classroom_data)
            session.add(classroom)
            session.commit()
            return classroom
    
    def update(self, classroom_id: int, classroom_data: dict):
        with SessionLocal() as session:
            classroom = session.query(Classroom).filter(Classroom.id_classroom == classroom_id).first()
            if classroom:
                for key, value in classroom_data.items():
                    setattr(classroom, key, value)
                session.commit()
            return classroom
    
    def delete(self, classroom_id: int):
        with SessionLocal() as session:
            classroom = session.query(Classroom).filter(Classroom.id_classroom == classroom_id).first()
            if classroom:
                session.delete(classroom)
                session.commit()
