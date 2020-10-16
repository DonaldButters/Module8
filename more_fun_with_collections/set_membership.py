def in_set():
    set_one = set('123456789')
    x = input("Please enter a set of numbers between 1-10 :")
    if x in set_one:
        print("Your answer is in the set!")
    else:
        print("Sorry, Your answer is not in the set.")
    print(set_one)


in_set()

