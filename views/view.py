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
    
    def get_int_input(self, prompt:str) -> int:
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please enter a valid integer")
    
