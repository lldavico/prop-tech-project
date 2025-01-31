
class Advertisement:

    def __init__(self, address: str, commune: str, tenant):
        self._address = address
        self._commune = commune
        self._tenant = tenant


    def __str__(self):
        return f"""Dirección: {self._address}
        Comuna: {self._commune}
        Arrendatario: {self._tenant.name} {self._tenant.lastname}
        Fecha de mudanza: {self._tenant.moving_date}
        """


