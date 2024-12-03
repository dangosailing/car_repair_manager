from models.repair import Repair
from database.repairs_db import RepairsDB
from views.view import View

class RepairsController:
    
    def __init__(self,repairs_db:RepairsDB, view:View) -> None:
        self.repairs_db = repairs_db
        self.view = view
        
    def run (self) -> None:
        while True:
            choice = self.view.display_menu(
                "Repair Management",
                {
                    "1": "Add Repair order",
                    "2": "View all Repair orders",
                    "3": "Delete Repair order",
                    "0": "Back to Main Menu"
                 }
            )
            
            if choice == "1":
                self.add_repair()
            elif choice == "2":
                self.view_all_repairs()
            elif choice == "3":
                self.delete_repair()
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid Choice. Please try again.")
                
    def add_repair(self) -> None:
        customer_id = int(self.view.get_input("Enter customer id: "))
        car_id = int(self.view.get_input("Enter car id: "))
        repair = Repair(customer_id,car_id)
        self.repairs_db.insert_repair(repair)
        self.view.display_message("Repair order added succesfully.")
        
    def view_all_repairs(self) -> None:
        repairs = self.repairs_db.fetch_all_repairs()
        self.view.display_items(repairs)
        
    def delete_repair(self) -> None:
        repair_id = self.view.get_int_input("Enter repair id to delete: ")
        self.repairs_db.delete_by_id(repair_id)
        self.view.display_message("Repair order deleted sucessfully.")
        
    