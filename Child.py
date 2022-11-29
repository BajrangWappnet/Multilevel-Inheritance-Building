
from sub_class import *

class Accessing(Customer):
 
       # constructor
       def __init__(self,name,customer_name,customer_idl):
            Customer.__init__(self,name,customer_name,customer_idl)
         
       # public member function
       def displayDetails(self):    
             # accessing protected data members of parent class
            print("Hotel Name: ", self._name)

             # accessing protected member functions of super class
            self._display_customer_name_and_id()



