# this is an example of python module

number_one = 1
age = 78


def print_hello():
    print('Hello!')


def times_four(pinter):
    print(pinter * 4)


class House:
    def __init__(self):
        self.type = input('what type of house:! ')
        self.height = input("What is the height in (Meters)? ")
        self.price = input("How much did it cost? ")
        self.age = input("How ol is it in years? ")

    def print_details(self):
        print("this is a a/n" + self.height)
        print(self.type, "house " + self.age, "years old and costing " + self.price + "dollars")
