from app.database.engine import engine
from app.database.base import Base

def init_db():
    Base.metadata.create_all(bind=engine)
    
def drop_all():
    Base.metadata.drop_all(bind=engine)