import os

class Building:
    
    # protected and private class variables 
    _name = None
    _floor = None
    
    # Using Constructor for filling up name and age of a person.
    def __init__(self,name):
        self._name = name
        self._floor = 0
        print("Hotel Details....")
        
    # Private class methods
    # Will take the self as parameter and will greet him/her with below message.
    def _greetings(self):
        print("Hello ! Welcome to " + self._name + "\nThis is greeting message from Person class.")
    
    # It will take self as parameter and ask for floor details
    # and will calculate age and print it. 
    def floor_details(self):
        y = input("Enter the floor no: ")
        self._floor = int(y)
        print()
        os.system("clear")
        print("Name of Hotel " + self._name + "and floor no is  " + str(self._floor))

