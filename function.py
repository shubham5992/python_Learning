# This script contains various functions for different calculations

# Function to calculate and print the sum of two numbers
def cal_sum(a, b):
    sum = a + b
    print(sum)
    return sum

# Function to calculate the sum of two numbers and return the result
def cal_sum_return(a, b):
    sum = a + b
    return sum

# Function to print the elements of a list
def print_list(list):
    for item in list:
        print(item, end=" ")

# Function to calculate factorial of a number
def fac(input):
    a, b = 0, 1
    for item in range(input):
        print(b, end=" ")
        a, b = b, a + b
        return item

# Function to calculate factorial of a number
def fact(n):
    result = 1
    for item in range(n, 1, -1):
        result *= item
    return result

# Function to convert USD to INR
def convert(n):
    rupees = 82 * n
    return rupees

# Function to check if a number is even or odd and return the result
def find_num(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

# Example usage
x = find_num(5)
print(x)
