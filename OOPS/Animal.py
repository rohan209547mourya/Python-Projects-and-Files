class Animal:
    def __init__(self):
        print("Animal Created")

    def who_am_i(self):
        print("I am an animal")

    def eat(self):
        print("I am eating")


class Cat(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("cat is created")


my_cat = Cat()
my_cat.eat()



