import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.database.base import Base
from app.database.engine import SessionLocal
from app.repositories.user_repository import UserRepository
from app.models.user import User

# ---------- Fixture pour une base SQLite en mémoire ----------
@pytest.fixture(scope="function")
def db_session():
    """Crée une base SQLite en mémoire, recrée les tables, et fournit une session.
    Remplace également la SessionLocal globale pour que le repository l'utilise.
    """
    engine = create_engine("sqlite:///:memory:", connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    original_session_local = SessionLocal
    import app.database.engine
    app.database.engine.SessionLocal = TestingSessionLocal
    
    session = TestingSessionLocal()
    try:
        yield session
    finally:
        session.close()
        app.database.engine.SessionLocal = original_session_local
        Base.metadata.drop_all(bind=engine)


# ---------- Tests ----------

def test_get_by_id_returns_user_when_found(db_session):
    # Arrange : insertion complète avec TOUS les champs obligatoires (évite le crash NOT NULL)
    user = User(id_user=42, name="Doe", first_name="John", email="john@example.com", password="hash", id_role=1)
    db_session.add(user)
    db_session.commit()

    repo = UserRepository()
    result = repo.get_by_id(42)

    # 🔧 CORRECTION : Vérifications strictes alignées avec l'objet inséré
    assert result is not None
    assert result.id_user == 42
    assert result.name == "Doe"
    assert result.first_name == "John"
    assert result.email == "john@example.com"


def test_get_by_id_returns_none_when_not_found(db_session):
    repo = UserRepository()
    result = repo.get_by_id(999)
    assert result is None


def test_get_by_email_returns_user_when_found(db_session):
    user = User(id_user=1, name="Doe", first_name="John", email="john@example.com", password="hash", id_role=1)
    db_session.add(user)
    db_session.commit()

    repo = UserRepository()
    result = repo.get_by_email("john@example.com")
    
    # 🔧 CORRECTION : validation complète de l'e-mail trouvé
    assert result is not None
    assert result.email == "john@example.com"


def test_get_by_email_returns_none_when_not_found(db_session):
    repo = UserRepository()
    result = repo.get_by_email("unknown@example.com")
    assert result is None


def test_add_hashes_password_and_creates_user(db_session):
    class UserCreateSimple:
        def __init__(self, name, first_name, email, password, id_role):
            self.name = name
            self.first_name = first_name
            self.email = email
            self.password = password
            self.id_role = id_role
        def model_dump(self):
            return {
                'name': self.name,
                'first_name': self.first_name,
                'email': self.email,
                'password': self.password,
                'id_role': self.id_role,
            }

    user_create = UserCreateSimple(
        name="Doe",
        first_name="Jane",
        email="jane@example.com",
        password="plaintextpassword",
        id_role=2
    )

    repo = UserRepository()
    result = repo.add(user_create)

    user_in_db = db_session.query(User).filter_by(email="jane@example.com").first()
    assert user_in_db is not None
    assert user_in_db.name == "Doe"
    assert user_in_db.first_name == "Jane"
    assert user_in_db.password != "plaintextpassword"


def test_update_existing_user_modifies_fields_and_commits(db_session):
    user = User(id_user=1, name="Doe", first_name="John", email="john@example.com", password="old_hash", id_role=1)
    db_session.add(user)
    db_session.commit()

    update_data = {"name": "Smith", "email": "smith@example.com", "id_role": 2}
    repo = UserRepository()
    result = repo.update(1, update_data)

    updated_user = db_session.query(User).filter_by(id_user=1).first()
    assert updated_user.name == "Smith"
    assert updated_user.email == "smith@example.com"
    assert updated_user.id_role == 2
    assert updated_user.first_name == "John"  # inchangé


def test_update_non_existing_user_returns_none(db_session):
    repo = UserRepository()
    result = repo.update(999, {"name": "Nobody"})
    assert result is None


def test_update_with_empty_data_still_commits(db_session):
    user = User(id_user=1, name="Doe", first_name="John", email="doe@example.com", password="hash", id_role=1)
    db_session.add(user)
    db_session.commit()

    repo = UserRepository()
    result = repo.update(1, {})

    updated_user = db_session.query(User).filter_by(id_user=1).first()
    assert updated_user.name == "Doe"


def test_delete_existing_user_returns_true_and_deletes(db_session):
    user = User(id_user=1, name="Doe", first_name="John", email="del@example.com", password="hash", id_role=1)
    db_session.add(user)
    db_session.commit()

    repo = UserRepository()
    result = repo.delete(1)

    assert result is True
    deleted_user = db_session.query(User).filter_by(id_user=1).first()
    assert deleted_user is None


def test_delete_non_existing_user_returns_false(db_session):
    repo = UserRepository()
    result = repo.delete(999)
    assert result is False