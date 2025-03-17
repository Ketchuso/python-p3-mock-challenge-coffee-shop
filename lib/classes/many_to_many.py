class Coffee:
    def __init__(self, name):
        if not isinstance(name, str): 
            raise TypeError("Value has to be a string")
        if len(name) < 3: 
            raise ValueError("Coffee name has to be 3+ characters long")
        
        self._name = name 

    @property
    def name(self):
        return self._name 

    @name.setter
    def name(self, new_value):
        raise AttributeError("Cannot change the name of the coffee.")
        

    def orders(self):
        pass
    
    def customers(self):
        pass
    
    def num_orders(self):
        pass
    
    def average_price(self):
        pass

class Customer:
    def __init__(self, name):
        self.name = name
        
    def orders(self):
        pass
    
    def coffees(self):
        pass
    
    def create_order(self, coffee, price):
        pass
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        if not isinstance(price, float):
            TypeError("Price must be a float")
        if price < 1.0 or price > 10.0:
            ValueError("Price must be a number from 1.0-10.0")
        self._price = price
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self, new_customer):
        raise AttributeError("Cannot change the customer")
    
    @property
    def coffee(self):
        return self._coffee
    
    @coffee.setter
    def coffee(self, new_coffee):
        raise AttributeError("Cannot change the coffee of this order.")
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError("Price must be a float")
        if new_price < 1.0 or new_price > 10.0:
            raise ValueError("Price must be a number from 1.0-10.0")
        self._price = new_price
    
