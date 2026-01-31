from backend import auth , sunny, windy, rainy, fall
app = True
print("="*100)
print("Welcome to weather guide app")
print("="*100)

print("Choose your weather code as following-\n1. Sunny\n2. Windy\n3. Rainy\n4. Fall\n")
code = input("Enter your code (1 to 4 numbers only): ")


while not auth(code):
    code = input("Renter your code (1 to 4 numbers only): ")
code = int(code)
# print(type(code))
print()

weather = None
if code == 1:
    sunny()
elif code == 2:
    windy()
elif code == 3:
    rainy()
elif code == 4:
    fall()