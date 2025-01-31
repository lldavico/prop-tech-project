

# Define una clase abstracta con ABC para las otras clases en los otros archivos
from abc import ABC, abstractmethod
from pydantic import BaseModel

class User(ABC):

    @abstractmethod
    def from_dict(cls, data: dict):
        NotImplementedError("Subclasses must implement this method")


class Customer(User, BaseModel):

    name: str
    lastname: str
    client_id: str

    @classmethod
    def _generate_client_id(cls, data: dict):
        client_id = f"{data['name']}_{data['lastname']}"
        return client_id

    @classmethod
    def from_dict(cls, data: dict):

        if data.get('name') is None:
            raise ValueError('name is required')
        
        if data.get('lastname') is None:
            raise ValueError('lastname is required')

        client_id = Customer._generate_client_id(data)
        data.update({'client_id': client_id})

        return cls(
            name=data['name'],
            lastname=data['lastname'],
            client_id=client_id
        )
    
    def __str__(self):
        return f'Im the {self.client_type} {self.client_id} called: {self.name} {self.lastname}'
