











class Protected:
    def __init__(self):
        self._age = 34


class Subclass(Protected):
    def display_age(self):
        print(self._age)

obj = Subclass()
obj.display_age()
'''print(obj._age)'''

class Private:
    def __init__(self):
        self.__salary = 50000  # Private attribute

    def salary(self):
        return self.__salary  # Access through public method

obj = Private()
print(obj.salary())  # Works
#print(obj.__salary)  # Raises AttributeError