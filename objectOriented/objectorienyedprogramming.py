##item1 = "Phone"
##item1_price = 100
##item1_quantity = 5
##item1_price_total = item1_price * item1_quantity
##

import csv 

#create a class
class Item:
    #global attributes = class attributes
    pay_rate = 0.8 #pay rate after 20% discount
    all = []

    
    #magic method
    #used everytime an instance is created
    #specify type - name: str - strings only for attribute name
    def __init__(self,name: str, price: float, quantity=0):
    # assert statements used to check what is happening vs expectations
        #Run validations to the received arguments
        assert price >=0, f"Price {price} is not greater than  or equal to zero"
        assert quantity >= 0, f"Quantity {quantity} is not greater than or equal to zero"


        
        print(f"an instance created: {name}")
        #using init method - can assign attributes within the method
        #instance attributes
        self.name = name
        self.price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)
        
        
    #create method without the paremeters using attributes
    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    #class method
    @classmethod
    def instantiate_from_csv(cls):
        with open('object.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity')),
                )
    #static method
    @staticmethod
    #object is not sent as first argument
    #static method like regular function that receives a parameter
    def is_integer(num):
        #count out floats that are .0
        if isinstance(num,float):
            #count out floats are are .0
            return num.is_integer()
        elif isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price},{self.quantity})"

    
#create methods - functions inside classes
#method needs parameter so instance can pass through
# def calculate_total_price(self,x,y):
   # return x * y

#child class
class Phone(Item):
    #all = []
    def __init__(self, name:str, price:float, quantity=0, broken_phones=0):
        #call to super function to have access to all attributes/methods
        super().__init__(
           name, price, quantity 
        )

        
        assert broken_phones >=0

        
        self.broken_phones = broken_phones

        #removing attribute at child class
        #using from parent class instead
        #Phone.all.append(self)
        
phone1 = Phone("phonev10",500,5, 1)
#phone1.broken_phones =1
phone1.calculate_total_price()
phone2 = Phone("phonev20",700,5,1)
#phone2.broken_phones =1


#creates an instance of a class
item1 = Item("Phone", 100, 5)
#random_str = str("4")- does same as above


#creating attributes
#each attribute is assigned to an instance of a class
#item1.name = "Phone"
#item1.price = 100
#item1.quantity = 5
#item1.calculate_total_price(item1.price, item1.quantity)




#print(type(item1))


item2 = Item("Laptop", 1000, 3)
#item2.name = "Laptop"
#item2.price = 1000
#item2.quantity = 3
#item2.calculate_total_price(item2.price, item2.quantity)



item3 = Item("Cable", 10, 5)
item4 = Item("Mouse", 50, 5)
item5 = Item("Keyboard", 75, 5)



#print(item1.name)

#print(Item.pay_rate)
#print(item1.pay_rate)


#Item.instantiate_from_csv()
#print(Item.all)

#Item.is_integer(7)
#Item.is_integer(7.5)
