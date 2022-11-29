from building import *

class Customer(Building):
    
    # Private class variables ::
    _customer_name = None
    _customer_id = None
    
    def __init__(self,name,customer_name,customer_id):
        Building.__init__(self,name)
        self._customer_name = customer_name
        self._customer_id = customer_id
      
    # Private class method ::
    def _display_customer_name_and_id(self):
        print("Name: ", self._customer_name)
        print("ID: ", self._customer_id)


