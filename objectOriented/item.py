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
        self.__name = name
        self.__price = price
        self.quantity = quantity

        #Actions to execute
        Item.all.append(self)



    @property
    def price(self):
        return self.__price
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def apply_increment(self, increment_value):
        self.__price = self.__price + self.__price * increment_value

    
    @property
    #property decorator = read-only attribute
    def name(self):
        return self.__name

    @name.setter
    def name(self,value):
        self.__name = value
        
    
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

    #hiding these instances from users
    # can only be called from class level
    def __connect(self, smtp_server):
        pass

    def __prepare_body(self):
        return f"""
        Hello
        """
    def __send(self):
        pass
    def send_email(self):
        self.__connect('')
        self.__prepare_body()
        self.__send()

    
##        @property
##        def read_only_name(self):
##            return "yoz'
