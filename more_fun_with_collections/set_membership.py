"""

Program: set_membership.py

Author: Donald Butters

Last date modified: 10/19/2020

The purpose of this program is to accept a set
and return a boolean value stating if the element is in the set

peram1 :accept a set

return :boolean value

"""
def in_set():
    set_one = set('123456789')
    x = input("Please enter a set of numbers between 1-10 :")
    if x in set_one:
        print("Your answer is in the set!")
    else:
        print("Sorry, Your answer is not in the set.")
    print(set_one)


in_set()

