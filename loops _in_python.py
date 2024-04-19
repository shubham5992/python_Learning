# This script contains examples of loops in Python

# Example 1: While loop
count = 1
while count <= 5:
    print("Sab sahi chal raha hai???") 
    count += 1

# Example 2: While loop printing numbers from 1 to 54544
i = 1
while i <= 54544:
    print("All is well", i)
    i += 1

# Example 3: While loop printing numbers from 1 to 100
i = 1
while i <= 100:
    print(i)
    i += 1

# Example 4: While loop printing numbers from 100 to 1
i = 100
while i >= 1:
    print(i)
    i -= 1

# Example 5: While loop to print the table of a number
n = int(input("Please enter a number to get its table: "))
i = 1
while i <= 10:
    print(n * i)
    i += 1

# Example 6: Repeat numbers in loop using for loop
items = ("mango", "orange", "pineapple", "banana")
for x in items:
    if x == "orange":
        break
    print(x)

# Example 7: Sum of numbers using range
n = 5
total_sum = 0
for i in range(1, n + 1):
    total_sum += i
print(total_sum)

# Example 8: Factorial of a number using while loop
n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("The value of factorial is:", fact)

# Example 9: Factorial of a number using for loop
n = 5 
fact = 1
for i in range(1, n + 1):
    fact *= i
print("The factorial of", n, "is:", fact)
