from models.car import Car
from database.cars_db import CarsDB
from views.view import View

class CarsController:
    
    def __init__(self,cars_db:CarsDB, view:View) -> None:
        self.cars_db = cars_db
        self.view = view
        
    def run (self) -> None:
        while True:
            choice = self.view.display_menu(
                "Car Management",
                {
                    "1": "Add Car",
                    "2": "View All Cars",
                    "3": "Delete Car",
                    "4": "Search by make",
                    "5": "Search by model",
                    "6": "Search by year",
                    "0": "Back to Main Menu"
                 }
            )
            
            if choice == "1":
                self.add_car()
            elif choice == "2":
                self.view_all_cars()
            elif choice == "3":
                self.delete_car()
            elif choice == "4":
                self.search_by_make()
            elif choice == "5":
                self.search_by_model()
            elif choice == "6":
                self.search_by_year()
            elif choice == "0":
                break
            else:
                self.view.display_message("Invalid Choice. Please try again.")
                
    def add_car(self) -> None:
        while True:
            try:
                make = self.view.get_input("Enter car make: ")
                self.view.validate_string(make)
                break
            except ValueError:
                print("Invalid input. Please enter car make")
        while True:
            try:
                model = self.view.get_input("Enter car model: ")
                self.view.validate_string(model)
                break
            except ValueError:
                print("Invalid input. Please enter car model: ")
        while True:
            try:
                year = self.view.get_input("Enter car year: ")
                self.view.validate_year(year)
                break
            except ValueError:
                print("Invalid input. Please enter a year: ")
        
        car = Car(make,model,year)
        self.cars_db.insert_car(car)
        self.view.display_message("Car added succesfully.")
        
    def view_all_cars(self) -> None:
        cars = self.cars_db.fetch_all_cars()
        self.view.display_items(cars)
        
    def delete_car(self) -> None:
        car_id = self.view.get_int_input("Enter car_id to delete: ")
        self.cars_db.delete_by_id(car_id)
        self.view.display_message("Car deleted sucessfully.")
        
    def search_by_make(self) -> None:
        make = self.view.get_input("Enter car make: ")
        cars = self.cars_db.search_by_make(make)
        self.view.display_items(cars)
    
    def search_by_model(self) -> None:
        model = self.view.get_input("Enter car model: ")
        cars = self.cars_db.search_by_model(model)
        self.view.display_items(cars)
    
    def search_by_year(self) -> None:
        year = self.view.get_int_input("Enter year: ")
        cars = self.cars_db.search_by_year(year)
        self.view.display_items(cars)
    