"""

Program: set_membership.py

Author: Donald Butters

Last date modified: 10/19/2020

The purpose of this program is use a function and dictionary to write case statement


peram1 :write and define functions
peram2 :save to dictionary
peram3 :write 4 other keys
return :impliment my switch

return :boolean value

"""
def add():
        result = A + B
        print(" Your numbers Added together = ",result,'   Thank you for doing math!')
        return result
def sub():
        result = A - B
        print("Your numbers subtracted from each other = ", result,'   Thank you for doing math!' )
        return result
def mul():
        result = A * B
        print("Your numbers multiplied together = ", result,'   Thank you for doing math!')
        return result
def div():
        result = A / B
        print("Your numbers divided by each other = ", result,'   Thank you for doing math!')
        return result
def dno():
        print("Your numbers are:",A,B,'    You did not do any math.')
def default():
        print('Sorry that is not an option')
def case_switch():
    A = int(input("Enter A Number : "))
    B = int(input("Enter Another Number : "))
    print('Would you like to do some math?')
    print("Enter 1 to: Add\nEnter 2 to: Subtract\nEnter 3 to: Multiply\nEnter 4 to: Divide\nEnter 5 to: Do Nothing  ")

    math = int(input("-Enter a number to do math! : "))

    def add():
        result = A + B
        print(" Your numbers Added together = ",result,'   Thank you for doing math!')
    def sub():
        result = A - B
        print("Your numbers subtracted from each other = ", result,'   Thank you for doing math!' )
    def mul():
        result = A * B
        print("Your numbers multiplied together = ", result,'   Thank you for doing math!')
    def dev():
        result = A / B
        print("Your numbers divided by each other = ", result,'   Thank you for doing math!')
    def dno():
        print("Your numbers are:",A,B,'    You did not do any math.')
    def default():
        print('Sorry that is not an option')

    funt = {1 : add,2 : sub,3 : mul,4 : div,5 : dno,}

    funt.get(math,default)()
A = int(input("Enter A Number : "))
B = int(input("Enter Another Number : "))


