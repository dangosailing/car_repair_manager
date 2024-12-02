from models.base import BaseModel

class Customer(BaseModel):
    
    def __init__(self, name: str, customer_id:int = None) -> None:
        self.name = name
        self.customer_id = customer_id
        