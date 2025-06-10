











class Protected:
    def __init__(self):
        self._age = 34


class Subclass(Protected):
    def display_age(self):
        print(self._age)

obj = Subclass()
obj.display_age()
'''print(obj._age)'''