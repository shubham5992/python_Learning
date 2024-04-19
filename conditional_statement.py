# This script contains examples of various conditional statements and calculations

# Traffic light control
light = input("light : ")
if light == "Red":
    print("We have to stop our vehicle")
elif light == "Yellow":
    print("We need to start our vehicle and be ready to go")
elif light == "Green":
    print("Get set go")
else:
    print("Report to the police")

# One-liner conditional statement
food = input("food : ")
eat = "Yes" if food == "cake" else "No"
print(eat)

# Ternary operator
age = int(input("age : "))
vote = "Yes" if age >= 18 else "No"
print(vote)

# Sum of two numbers
a = int(input("Enter the value 1: "))
b = int(input("Enter the value 2: "))
sum = a + b
print(sum)

# Area of a square
side = int(input("Please enter the side of square: "))
area = side * side
print(area)

# Average of two numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
average = (a + b) / 2
print(average)
