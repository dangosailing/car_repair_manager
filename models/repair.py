from models.base import BaseModel

class Repair(BaseModel):
    
    def __init__(self, customer_id: int, car_id:int, customer_name:str = None, car_info:str = None, repair_id:int = None) -> None:
        self.customer_id = customer_id
        self.car_id = car_id
        self.customer_name = customer_name
        self.car_info = car_info
        self.repair_id = repair_id