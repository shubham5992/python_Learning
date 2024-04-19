# This script contains examples of various loops and calculations

# Print numbers from 1 to 10 using a for loop:
for i in range(1, 11):
    print(i)

# Calculate the sum of numbers from 1 to 10 using a for loop:
sum = 0
for i in range(1, 11):
    sum += i
print("The sum of numbers from 1 to 10 is:", sum)

# Calculate the product of elements in a list using a for loop:
product = 1
my_list = [2, 4, 5, 6, 8, 3]
for num in my_list:
    product *= num
print(product)

# Print even numbers from 1 to 10 using a for loop:
for i in range(2, 11, 2):
    print(i)

# Find the largest number in a list:
my_list = [3, 9, 1, 6, 2, 8]
largest = max(my_list)
print(largest)

# Find the average of numbers in a list using a for loop:
sum = 0
my_list = [4, 7, 9, 2, 5]
for num in my_list:
    sum += num
avg = sum / len(my_list)
print(avg)

# Print uppercase letters in a string:
my_string = "Hello World"
for char in my_string:
    if char.isupper():
        print(char)

# Count the number of vowels in a string using a for loop:
count = 0
str = "Hello World"
vowels = "AEIOUaeiou"
for char in str:
    if char in vowels:
        count += 1
print(count)

# Print a pattern using nested loops:
for i in range(5):
    for j in range(i + 1):
        print("*", end="")
    print()

# Print squares of numbers from 1 to 5:
squares = [num ** 2 for num in range(1, 6)]
print(squares)

# Print numbers divisible by 3 or 5 from 1 to 20:
for num in range(1, 21):
    if num % 3 == 0 or num % 5 == 0:
        print(num)

# Fibonacci series using while loop:
a, b = 0, 1
count = 0
while count < 10:
    print(a, end=" ")
    a, b = b, a + b
    count += 1

# Find the common elements in two lists using a for loop:
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = [el for el in list1 if el in list2]
print(common_elements)

# Print non-negative numbers from a list using a while loop:
my_list = [1, 4, 6, 8, 10, -3, 5, 7]
index = 0
while my_list[index] >= 0:
    print(my_list[index])
    index += 1

# Print numbers from 1 to 10 and break the loop if a number divisible by 4 is encountered:
for num in range(1, 11):
    print(num)
    if num % 4 == 0:
        break

# Check if a number is prime or not:
num = int(input("Please enter a number to check whether it's prime or not: "))
if num < 2:
    print("The number is not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
