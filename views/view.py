class View:
    def display_menu(self, title:str, options:dict) -> str:
        print(f"\n{title}")
        for key, description in options.items():
            print(f"{key}) {description}")
        return input("Choose an option: ")
    
    def display_message(self, message:str) -> None:
        print(message)
    
    def display_items(self, items:list) -> None:
        if not items:
            print("No items to display.")
        else:
            for item in items:
                print(str(item))
    
    def get_input(self, prompt:str) -> str:
        return input(prompt)
    
    def validate_year(self, input_year:str) -> bool:
        if input_year and input_year.isdigit() and int(input_year) > 1900:
            return input_year 
        else:
            raise ValueError("Error: You need to enter a valid input")
    
    def validate_string(self, input_str:str) -> str:
        if input_str and input_str != "" and input_str != None:
            return input_str
        else:
            raise ValueError("Error: You need to enter a valid input")
            
        
    def get_int_input(self, prompt:str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer")
    
