from datetime import datetime

from src.entities.advertisement import Advertisement
from src.entities.user import Customer


class Tenant(Customer):

    _client_type: str = 'tenant'
    _moving_date: datetime = None

    def _set_moving_date(self, moving_date: datetime):
        self._moving_date = moving_date

    @property
    def moving_date(self):
        if self._moving_date is None:
            self._set_moving_date(datetime.now())
        return self._moving_date
    
    

    
