from order import Order
from customer import Customer
class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name (self):
      return self._name
    
    @name.setter
    def name(self,value):
       if isinstance (value,str)and 1<=len(value)<=15:
          return self._value
       else:
          raise ValueError("Customer must be of input string and must be between 1 and 15 characters")
       

    def orders(self):
        return [order for order in Order.all_orders if order.coffee == self]
        
    def coffees(self):
       return list(set(order.coffee for order in self.orders()))

    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
    def most_aficionado(coffee):
       