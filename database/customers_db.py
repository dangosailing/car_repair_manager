from database.db import Database
from models.customer import Customer
from typing import List

class CustomersDB:
    def __init__(self, db:Database) -> None:
        self.db = db
    
    def insert_customer(self, customer:Customer) -> None:
        query = """INSERT INTO customers (name)
        VALUES(?);"""
        self.db.execute_query(query, (customer.name,))
        
    def fetch_all_customers(self) -> List[Customer]:
        query = "SELECT * FROM customers;"
        rows = self.db.fetch_all(query)
        return [Customer(row["name"], row["customer_id"]) for row in rows]
    
    def delete_by_id(self,customer_id:int) -> None:
        query = "DELETE FROM customers WHERE customer_id = ?;"
        self.db.execute_query(query, (customer_id,))
        
        