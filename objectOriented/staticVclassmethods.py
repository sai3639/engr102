# class vs static methods

class Item:
    @staticmethod
    def is_integer(num):
        pass
        #should do something that has a relationship with the class
        #not something that is unique per instance

    @classmethod
    def instansiate_from_something(cls):
        pass
        #should do something that has a relationship with the class
        #used to manipulate different structures of data to insantiate
            #objects  - like with csv

    #static v class
    #static does not pass the first object reference as the first argument
        



