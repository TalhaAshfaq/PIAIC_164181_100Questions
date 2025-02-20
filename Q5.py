class User:
    def __init__(self):
        self.user_input = ""

    def getstring(self):
        self.user_input = input("Please Enter a string")

    def printstring(self):
        print(f"user input is: {self.user_input.upper()}")

s1 = User()

def test():
    s1.getstring()
    s1.printstring()

test()