from app.database.seeders.roles_seeder import seed_roles
from app.database.seeders.buildings_seeder import seed_buildings
from app.database.seeders.floors_seeder import seed_floors
from app.database.seeders.rooms_seeder import seed_rooms


def seed_all():
    seed_roles()
    seed_buildings()
    seed_floors()
    seed_rooms()


if __name__ == "__main__":
    seed_all()
