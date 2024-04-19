# This script contains examples of string methods and some practice exercises

# Example 1: String methods
str = "apna college" 
print(str[:len(str)])
print(str.capitalize())
print(str.replace("p", "o"))
print(str.find("apna"))
print(str.count("o"))

# Practice Exercise: Name length
name = input("What is your name: ")
print("Length of your name:", len(name))

# Practice Exercise: Check if a number is even or odd
num = int(input("Please enter a number: "))
if num % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")

# Practice Exercise: Check if a number is a multiple of 7
num = int(input("Please enter a number: "))
if num % 7 == 0:
    print("Number is a multiple of 7")
else:
    print("Number is not a multiple of 7")

# Practice Exercise: Find the biggest number among three numbers
a = int(input("Please enter the first number: "))
b = int(input("Please enter the second number: "))
c = int(input("Please enter the third number: "))
if a >= b and a >= c:
    print("The biggest number is:", a)
elif b >= c:
    print("The biggest number is:", b)
else:
    print("The biggest number is:", c)

# Practice Exercise: Find the biggest number among four numbers
a = float(input("Please enter the first number: "))
b = float(input("Please enter the second number: "))
c = float(input("Please enter the third number: "))
d = float(input("Please enter the fourth number: "))
greatest_number = max(a, b, c, d)
print("The greatest number is:", greatest_number)
