class public:
    def __init__(self):
        self.name = "Docteur"

    def display_name(self):
        print(self.name)

obj = public()
obj.display_name()
print(obj.name)