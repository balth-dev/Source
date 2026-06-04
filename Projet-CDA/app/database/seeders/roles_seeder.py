from app.database.engine import SessionLocal
from app.models.role import Role

def seed_roles():
    with SessionLocal() as session:
        if session.query(Role).count() > 0:
            print("Les rôles existent déjà dans la base de données.")
            return

        roles_to_add = [
            Role(id_role=2, name="admin"),
            Role(id_role=3, name="gestionnaire"),
            Role(id_role=4, name="enseignant"),
            Role(id_role=5, name="etudiant"),
            Role(id_role=6, name="technicien")
        ]

        session.add_all(roles_to_add)
        session.commit()
        print("Rôles semés avec succès en parfaite conformité avec ROLE_MAPPING !")

if __name__ == "__main__":
    seed_roles()