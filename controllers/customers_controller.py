from models.customer import Customer
from database.customers_db import CustomersDB
from views.view import View

class CustomersController:
    
    def __init__(self,customers_db:CustomersDB, view:View) -> None:
        self.customers_db = customers_db
        self.view = view
        
    def run (self) -> None:
        while True:
            choice = self.view.display_menu(
                "Customer Management",
                {
                    "1": "Add Customer",
                    "2": "View All Customers",
                    "3": "Delete Customer",
                    "0": "Back to Main Menu"
                 }
            )
            
            if choice == "1":
                self.add_customer()
            elif choice == "2":
                self.view_all_customers()
            elif choice == "3":
                self.delete_customer()
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid Choice. Please try again.")
                
    def add_customer(self) -> None:
        while True:
            try:
                name = self.view.get_input("Enter customer name: ")
                self.view.validate_string(name)
                break
            except ValueError:
                print("Invalid input. Please enter customer name: ")
        customer = Customer(name)
        self.customers_db.insert_customer(customer)
        self.view.display_message("Customer added succesfully.")
        
    def view_all_customers(self) -> None:
        customers = self.customers_db.fetch_all_customers()
        self.view.display_items(customers)
        
    def delete_customer(self) -> None:
        customer_id = self.view.get_int_input("Enter customer_id to delete: ")
        self.customers_db.delete_by_id(customer_id)
        self.view.display_message("Customer deleted sucessfully.")
        
    