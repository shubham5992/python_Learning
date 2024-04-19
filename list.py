# This script contains examples of lists, tuples, and an exercise

# Example 1: Lists
# marks = [10, 545, 454545, 34, 54, 343, 3434]
# marks.append(5434444)
# print(marks)
# marks.sort()
# print(marks)
# marks.insert(0, 777777)
# print(marks)
# marks.remove(777777)
# print(marks)
# marks.pop(0)
# print(marks)

# Example 2: Tuples
# marks = (3434, 34, 454, 4545, 454, 456)
# print(marks.index(454))
# print(marks.count(34))

# Exercise: Create a list of movies
# movies = []
# movie1 = input("Write the first movie: ")
# movie2 = input("Write the second movie: ")
# movie3 = input("Write the third movie: ")
# movies.extend([movie1, movie2, movie3])
# print(movies)

# Exercise: Check palindrome
list1 = [1, 3, 1]
list2 = [4, 4, 2]

list1_copy = list1.copy()
list1_copy.reverse()
print(list1_copy)

if list1_copy == list1:
    print("Palindrome")
else:
    print("NOT PALINDROME")

# Exercise: Sum of numbers
n = 10
total_sum = 0
for i in range(n + 1):
    total_sum += i
    print(total_sum)
