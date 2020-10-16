def in_dict():
    dict_one = {'Donald':85,'Daniel':84,'Manji':86, 'Holly':91 }
    x = input("Please enter Your Name :")
    if x in dict_one:
        print("Your Name is in the directory!")
        for key, value in dict_one.items():
            print(key, ' : ', value)
    else:
        print("Sorry, Your name is not in the directory.")



in_dict()
