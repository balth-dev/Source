from app.database.engine import SessionLocal
from app.models.building import Building
from app.models.floor import Floor

def seed_floors():
    with SessionLocal() as session:
        if session.query(Floor).count() > 0:
            print("Les étages existent déjà dans la base de données.")
            return

        bat_k1 = session.query(Building).filter_by(name="K1").first()
        bat_k2 = session.query(Building).filter_by(name="K2").first()

        if not bat_k1 or not bat_k2:
            print("Erreur : Les bâtiments indispensables (K1 ou K2) n'existent pas.")
            print("Lancez d'abord : python -m app.database.seeders.buildings_seeder")
            return

        floors_to_add = [
            Floor(number=0, building_id=bat_k1.id_building), # RDC
            Floor(number=1, building_id=bat_k1.id_building), # 1er étage
            Floor(number=2, building_id=bat_k1.id_building), # 2ème étage
            Floor(number=0, building_id=bat_k2.id_building), # RDC
            Floor(number=1, building_id=bat_k2.id_building)  # 1er étage
        ]

        session.add_all(floors_to_add)
        session.commit()
        print("Étages semés avec succès ! (Bâtiment K1 : RDC, 1, 2 | Bâtiment K2 : RDC, 1)")

if __name__ == "__main__":
    seed_floors()