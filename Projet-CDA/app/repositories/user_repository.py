from bcrypt import gensalt, hashpw

from ..database.engine import SessionLocal
from ..models.user import User
from ..validators.user_validator import UserCreate


class UserRepository:
    def get_all(self) -> list[User]:
        with SessionLocal() as session:
            return session.query(User).all()
    
    def get_by_id(self, user_id: int) -> User | None:
        with SessionLocal() as session:
            return session.query(User).filter(User.id_user == user_id).first()
    
    def get_by_email(self, email: str) -> User | None:
        with SessionLocal() as session:
            return session.query(User).filter(User.email == email).first()
        
    def add(self, user_create: UserCreate):
        with SessionLocal() as session:
            user_data = user_create.model_dump()
            hashed_password = hashpw(user_data['password'].encode('utf-8'), gensalt()).decode('utf-8')

            # Mapper les champs du validateur aux colonnes du modèle
            user = User(
                name=user_data.get('name'),
                first_name=user_data.get('surname'),
                email=user_data.get('mail'),
                password=hashed_password,
                gender=user_data.get('gender'),
                id_role=user_data.get('id_role'),
            )
            session.add(user)
            session.commit()
    
    def update(self, user_id: int, user_data: dict):
        with SessionLocal() as session:
            user = session.query(User).filter(User.id_user == user_id).first()
            if user:
                for key, value in user_data.items():
                    setattr(user, key, value)
                session.commit()
            return user
    
    def delete(self, user_id: int):
        with SessionLocal() as session:
            user = session.query(User).filter(User.id_user == user_id).first()
            if user:
                session.delete(user)
                session.commit()
                return True
            return False