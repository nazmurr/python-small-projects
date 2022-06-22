'''
- show temperature main menu
- take user input for temp
- convert temp to fahrenheit or celsius
- show output
- use oop system
'''

class TemperatureConverter:
    def __init__(self):
        self.menu_choice = None
        self.temperature_input = 0
        self.input_unit = None
        self.output_unit = None
        
    def to_fahrenheit(self):
        return (self.temperature_input * 9/5) + 32

    def to_celsius(self):
        return (self.temperature_input - 32) * 5/9

    def show_menu(self):
        menu = "1. Convert Fahrenheit to Celsius\n2. Convert Celsius to Fahrenheit\n"
        print(menu)
        while True:
            self.menu_choice = input("Select an option [1 or 2]: ")
            if self.menu_choice == "1":
                self.input_unit = "F"
                self.output_unit = "C"
                break

            if self.menu_choice == "2":
                self.input_unit = "C"
                self.output_unit = "F"
                break

        while True:
            try:
                self.temperature_input = float(input(f"Enter temperature ({self.input_unit}): "))
                if self.menu_choice == "1":
                    print(str(self.temperature_input) + "°" + self.input_unit 
                    + " is " + str(self.to_celsius()) + "°" + self.output_unit)
                if self.menu_choice == "2":
                    print(str(self.temperature_input) + "°" + self.input_unit 
                    + " is " + str(self.to_fahrenheit()) + "°" + self.output_unit)
                break
            except ValueError:
                print("Please enter only number")
        
temperature_converter = TemperatureConverter()
temperature_converter.show_menu()
