from database.db import Database
from database.cars_db import CarsDB
from database.customers_db import CustomersDB
from database.repairs_db import RepairsDB
from controllers.cars_controller import CarsController
from controllers.customers_controller import CustomersController
from controllers.repairs_controller import RepairsController

from views.view import View

class MainController:
    
    def __init__(self, db:Database, view:View) -> None:
        self.db = db
        self.cars_db = CarsDB(db)
        self.customers_db = CustomersDB(db)
        self.repairs_db = RepairsDB(db)
        self.view = view
        
    def run(self) -> None:
        while True:
            choice = self.view.display_menu(
                "Main menu",
                {
                    "1": "Manage cars",
                    "2": "Manage customers",
                    "3": "Manage repair orders",
                    "0": "Exit"
                }
            )
            
            if choice == "1":
                cars_controller = CarsController(self.cars_db, self.view)
                cars_controller.run()
            if choice == "2":
                customers_controller = CustomersController(self.customers_db, self.view)
                customers_controller.run()
            if choice == "3":
                 repairs_controller= RepairsController(self.repairs_db, self.view)
                 repairs_controller.run()
            elif choice == "0":
                self.view.display_message("Exiting the application. Goodbye!")
                break
            else:
                self.view.display_message("Invalid choice. Please try again")