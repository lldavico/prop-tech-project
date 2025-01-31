from src.entities import Tenant, Independizer


i1 = Independizer.from_dict({
    'name': 'juan',
    'lastname': 'perez'
})

t1 = Tenant.from_dict({
    'name': 'pedro',
    'lastname': 'perez'
})

t2 = Tenant.from_dict({
    'name': 'made',
    'lastname': 'sequea'
})



def get_users() -> list:
    return [
            i1, 
            t1,
            t2,
        ]