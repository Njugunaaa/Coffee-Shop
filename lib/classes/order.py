from customer import Customer
from coffee import Coffee
class Order:
    all_orders=[]               
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if isinstance(value, float) and 1.0 <= value <= 10.0:
            self._price = value
        else:
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        

    @property
    def customer(self):
        return self._customer
    @customer.setter
    def customer(self,value):
        
        if isinstance(value,Customer):
            self._customer

        else:
            raise TypeError("Customer should be an instance of a customer. ")

    @property
    def coffee(self):
        return self._coffee
    @coffee.setter
    def coffee(self,value):
        if isinstance(value,Coffee):
            self._coffee

        else:
            raise TypeError("Coffee should be an instance of a coffee. ")        

    

