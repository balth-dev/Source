from app.database.engine import SessionLocal
from app.models.building import Building

def seed_buildings():
    with SessionLocal() as session:
        if session.query(Building).count() > 0:
            print("Les bâtiments existent déjà.")
            return

        bat_K1 = Building(name="K1")
        bat_K2 = Building(name="K2")
        session.add_all([bat_K1, bat_K2])
        session.commit()
        print("Bâtiments semés avec succès !")

if __name__ == "__main__":
    seed_buildings()