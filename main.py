from database.db import Database
from controllers.app_controller import MainController
from views.view import View



def main():
    db = Database()
    db.connect()
    db.setup_tables()
    
    the_view = View()
    
    the_main_controller = MainController(db, the_view)
    the_main_controller.run()
    
    db.close()
    
if __name__ == "__main__":
    main()