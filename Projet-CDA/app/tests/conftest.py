from dotenv import load_dotenv
import pytest

from app.database.init_db import drop_all, init_db
from app.models import *

@pytest.fixture(scope="session", autouse=True)
def test_setup_env():
    load_dotenv("tests/ .env.test", override=True)
    
@pytest.fixture(scope="function", autouse=True)
def test_setup_database():
    drop_all()
    init_db()
    yield
    drop_all()