# When to use class methods and when to use static methods?

class Item:
    @staticmethod
    def is_integer():
        """

        This should do something that has a relationship
        with the class, but not something that must be a unique
        per instance!

        """
    @classmethod
    def instantiate_from_something(cls):
        """

        This should also do something that has a relationship
        with the class, but usually, those are used to
        manipulate different structures of data to instantiate
        objects, like we have done with csv.

        """

# However, those could be also called from instance.
class Item:
    def is_integer(self, value):
        return isinstance(value, int)

    def instantiate_from_something(self):
        # Example implementation of this method
        pass

item1 = Item()
item1.is_integer(5)  # This method is called, but no output is printed
item1.instantiate_from_something()
# item1 = Item()
# item1.is_integer(5)
# item1.instantiate_from_something()