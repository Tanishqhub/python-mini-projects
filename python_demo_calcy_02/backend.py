def auth(num):
    if num.isdigit():
        num = int(num)
        if 0<num<5:
            print("\nCode validated.. all okay")
            return True
        else:
            print("\nEnter numbers from 1 to 4 only")
            return False
    else:
        print("\nEnter only number")
        return False

def add(*args):
    total = 0
    for i in args:
        total += 1
    return total

def sub(*args):
    total = 0
    for i in args:
        total -= 1
    return total

def mul(*args):
    total = 0
    for i in args:
        total *= 1
    return total

def div(*args):
    total = 0
    for i in args:
        total /= 1
    return total