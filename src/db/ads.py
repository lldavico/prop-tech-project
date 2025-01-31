from src.db.users import t1, t2, i1
from src.entities.advertisement import Advertisement


p1 = Advertisement(
    address='Isidora Goyenechea 1013, depto 1014',
    commune='Las Condes',
    tenant=t1
)

p2 = Advertisement(
    address='La Capitanía 70, depto 1015',
    commune='Las Condes',
    tenant=t2
)


def get_ads() -> list:
    return [
        p1,
        p2
    ]