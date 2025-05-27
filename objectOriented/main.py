from item import Item
from phone import Phone

##Item.instantiate_from_csv()
##
##print(Item.all)


#encapsulation 

item1 = Item("MyItem",760)
##item1.name = "OtherItem"
##
##print(item1.read_only_name)

#private attribute

#setting an attribute
item1.name = "OtherItem"

#getting an attribute
#print(item1.name)

#encapsulation
#restricting direct access to some attributes in the program

#abstraction
#only shows necessary attributes - hides unnecessary details from users

item1.send_email()

#inheritance - can reuse code across our classes

#polymorphism - use a single type identity to represent different types
#in different scenarios
