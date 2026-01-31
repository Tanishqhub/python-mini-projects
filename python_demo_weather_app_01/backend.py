def auth(num):
    if num.isdigit():
        num = int(num)
        if 0 < num < 5:
            print("Code verified.. all ok")
            return True
        else:
            print("Enter numbers from 1 to 4 only")
            return False
    else:
        print("Enter only numbers")
        return False

def sunny():
    print("Sunny app is working\n")
    print("Choose What you have-\n1. Cap\n2. None of the above")
    choice = input("Enter your choice code: ")
    while not auth(choice):
        choice = input("Renter your choice code: ")
    choice = int(choice)
    print(f"You chose {choice}\n")
    if choice == 1:
        print("Wear cap")
    elif choice == 2:
        print("Stay home stay safe")


def windy():
    print("Windy app is working\n")
    print("Choose What you have-\n1. Jacket\n2. None of the above")
    choice = input("Enter your choice code: ")
    while not auth(choice):
        choice = input("Renter your choice code: ")
    choice = int(choice)
    print(f"You chose {choice}\n")
    if choice == 1:
        print("Wear Jacket")
    elif choice == 2:
        print("Stay home stay safe")

def rainy():
    print("Rainy app is working\n")
    print("Choose What you have-\n1. Raincoat\n2. Umbrella\n3. None of the above")
    choice = input("Enter your choice code: ")
    while not auth(choice):
        choice = input("Renter your choice code: ")
    choice = int(choice)
    print(f"You chose {choice}\n")
    if choice == 1:
        print("Wear Raincoat")
    if choice == 2:
        print("Use Umbrella")
    elif choice == 3:
        print("Stay home stay safe")

def fall():
    print("Fall app is working")
    print("Enjoy the weather as it is")
