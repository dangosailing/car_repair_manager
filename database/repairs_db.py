from database.db import Database
from models.repair import Repair
from typing import List

class RepairsDB:
    def __init__(self, db:Database) -> None:
        self.db = db
    
    def insert_repair(self, repair:Repair) -> None:
        query = """INSERT INTO repairs (customer_id, car_id)
        VALUES(?,?);"""
        self.db.execute_query(query, (repair.customer_id, repair.car_id))
        
    def fetch_all_repairs(self) -> List[Repair]:
        query ="SELECT * FROM repairs INNER JOIN customers on repairs.customer_id = customers.customer_id INNER JOIN cars on repairs.car_id = cars.car_id;"
        rows = self.db.fetch_all(query)
        for row in rows:
            print(row["customer_id"], row["car_id"], row["name"], f"{row["model"]} - {row["make"]}")
        return [Repair(row["customer_id"], row["car_id"], row["name"], f"{row["model"]} - {row["make"]}", row["repair_id"]) for row in rows]
    
    def delete_by_id(self,repair_id:int) -> None:
        query = "DELETE FROM Repairs WHERE repair_id = ?;"
        self.db.execute_query(query, (repair_id,))
        
        