from backend import *

print("="*50)
print("Welcome to dumb calcy")
print("="*50)

print("\nChoose from the following operation-\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
op = input("Enter your operation code: ")

while not auth(op):
    op = input("Renter your operation code: ")
op = int(op)

if op == 1:
    user = input("Enter a series of number separated by a comma (,): ")
    nums = user.split(",")
    print(i for i in nums)