# Comprehensive list:
# Write a list comprehension to generate squares of numbers from 1 to 10.

l1 = [i**2 for i in range(1,11)]
print(l1)


# 2. Create a list of even numbers between 1 and 50 using list
# comprehension.

l2 = [i for i in range(1,50) if i%2 == 0]
print(l2)

# 3. Convert all strings in a list to uppercase using list comprehension.

l3 = ['abc','efg']
new_l3 = [x.upper() for x in l3]
print(new_l3)

# 4. Given a list of integers, create a new list that contains only the positive
# numbers.

l4 = [0, 2, 7, 1, -4, 2, -1]
new_l4 = [x for x in l4 if x > 0]
print(new_l4)


# 5. Create a list of tuples (num, num^2) for numbers 1 to 5.

l5 = [(x, x**2) for x in range(1,5)]
print(l5)


# 6. Extract all vowels from a given string using list comprehension.

str1 = 'rachana'
l6 = [x for x in str1 if x.lower() in 'aeiou']
print(l6)

# 7. Flatten a 2D list using list comprehension.

l7 = [[1,2,3],[4,5,6],[7,8,9]]
new_l7 = [x for row in l7 for x in row]
print(new_l7)

# 8. Replace all negative numbers in a list with 0 using list comprehension.

l8 = [0, 2, 7, 1, -4, 2, -1]
new_l8 = [0 if x < 0 else x for x in l8]
print(new_l8)


# 9. Given a list of words, create a list of lengths of each word.

l9 = ['rachana', 'apple', 'orange', 'abc',1,2]
new_l9 = [len(x) for x in l9 if type(x) == str]
print(new_l9)

# 10. Filter out words that start with the letter 'A' or 'a'.

l10 = ['rachana', 'apple', 'orange', 'abc']
new_l10 = [x for x in l10 if x.lower().startswith('a')]
print(new_l10)


# 11. From a list of numbers, generate a list of “even” or “odd” strings using
# list comprehension.
# (Like → [“even”, “odd”, “odd”, “even”…])

l11 = [1,2,3,4,5,6,7,8]
new_l11 = ['even' if x%2 == 0 else 'odd' for x in l11]
print(new_l11)

# 12. Create a list of numbers divisible by both 3 and 5 in range 1–100.

l12 = [x for x in range(1,100) if x%3 == 0 and x%5 == 0]
print(l12)

# 13. Write a nested list comprehension to generate a multiplication table
# for 1–5.

l13 = [[i*j for j in range(1,6)] for i in range(1,6)]
print(l13)

for i in range(1,6):
    row = []
    for j in range(1,6):
        row.append(i*j)
    print(row)


# 14. Convert a dictionary’s keys into a list using list comprehension.
dict1 = {'1':'apple', '2': 'orange', '3': 'grape'}
l1 = [i for i in dict1]
print(l1)


# 15. Extract numeric digits from a string using list comprehension.

s = 'abc 1 cb 2 3'
digits = [x for x in s if x.isdigit()]
print(digits)

# 16. Use list comprehension to remove all spaces from a string.

s = 'abc 1 cb 2 3'
spaces = [ch for ch in s if ch != ' ']
print("".join(spaces))


# 17. Create a list of characters that appear more than once in a string.

s = 'abc 1 cb 2 3'
new_s = [x for x in s if s.count(x) > 1]
print(new_s)


# 18. From a list of sentences, generate a list of all words (split using list
# comprehension).

sentences = [
    "I am rachana",
    "I am learning python"

]

words = [x for sentence in sentences for x in sentence.split()]
print(words)


# 19. Create a list of unique elements from a list using list comprehension +
# condition.

num = [1,2,2,3,6,4,4,7]

unique_num = list({x for x in num})
print(unique_num)

# 20. Generate all pairs (x, y) where x is from list A and y is from list B
# (cartesian product).

A = [1,2,3,5]
B = [4,0,7]

pairs = [(x,y) for x in A for y in B]
print(pairs)


# Lambda functions
# 1. Write a lambda to add two numbers.

x, y = 2,3
add = lambda x: x + y
print(add(x))


# 2. Create a lambda to check if a number is even.

even = lambda x: 'even' if x%2 == 0 else 'odd'
print(even(5))

# 3. Write a lambda to get the last character of a string.

last_char = lambda x: x[-1]
print(last_char('rachana'))

# 4. Use lambda with map() to square every number in a list.

l1 = [1,2,3,5]
squares = list(map(lambda x : x**2, l1))
print(squares)


# 5. Use lambda with filter() to get only odd numbers from a list.
l1 = [1,2,3,5]
odds = list(filter(lambda x: x%2 != 0, l1))
print(odds)

# 6. Use sorted() + lambda to sort a list of tuples by second value.

l1 = [(1, 5), (2, 3), (4, 1), (3, 9)]
sorted_l1 = sorted(l1, key=lambda x: x[1])
print(sorted_l1)

# 7. Create a lambda to check if a string is a palindrome.
# 8. Use lambda to find maximum of three numbers.

max_num= lambda a, b, c: max(a, b, c)
print(max_num(10, 25, 15))


# 9. Write a lambda to reverse a string.

reverse_str = lambda s: s[::-1]
print(reverse_str("rachana"))

# 10. Use lambda with map() to convert a list of strings to integers.

nums = ["10", "20", "30", "40"]
int_nums = list(map(lambda x: int(x), nums))
print(int_nums)


# 11. Use lambda with filter() to remove empty strings from a list.

non_empty = lambda x: x != ""
print(list(filter(non_empty, ["a", "", "b", ""])))


# 12. Use lambda to compute factorial using reduce() (yeah, that one-liner
# madness).

import functools
from functools import reduce
factorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1), 1)
print(factorial(5))


# 13. Write a lambda that returns the larger of two numbers.

larger = lambda a, b: a if a > b else b
print(larger(10, 7))

# 14. Use lambda to check if number is divisible by 5.

div_by_5 = lambda x: x % 5 == 0
print(div_by_5(25))

# 15. Use lambda + map() to add 10 to each element of a list.

add_10 = lambda x: x + 10
print(list(map(add_10, [1, 2, 3])))


# 16. Use lambda to sort a list of dictionaries by a key (like "age").

people = [{"name": "A", "age": 30}, {"name": "B", "age": 25}]
print(sorted(people, key=lambda x: x["age"]))


# 17. Write a lambda that returns True if a character is a vowel.

vowels = lambda c: c.lower() in "aeiou"
print(vowels("A"))


# 18. Use lambda + filter to extract words of length > 5 from a list.

lengths = lambda w: len(w) > 5
print(list(filter(lengths, ["python", "java", "rachana"])))

# 19. Use lambda to calculate the area of a circle (πr²).

circle_area = lambda x : 3.14 * x * x
print(circle_area(5))

# 20. Write a lambda to remove duplicates from a list using filter + set.

l1 = [1,2,2,3,4,5,6,6]
duplicates = lambda x : set(x)
print(duplicates(l1))

set1 = set({})
duplicates = lambda x: x not in set1 and not set1.add(x)
print(list(filter(duplicates, [1,2,2,3,4,5,6,6])))

# 21. Use lambda with reduce() to find the product of all numbers in a list.

from functools import reduce

nums = [2, 3, 4, 5]

product = reduce(lambda x, y: x * y, nums)
print(product)

# 22. Write a lambda that returns absolute value of a number.

ab_val = lambda x: x if x >= 0 else -x

print(ab_val(-7))

# 23. Use lambda to sort a list of strings by their length.

l1 = ["apple", "kiwi", "banana", "fig"]

sorted_l1 = sorted(l1, key=lambda x: len(x))
print(sorted_l1)

# 24. Use lambda to get only uppercase characters from a string.

text = "RacHanA cHAvaN"

upper = list(filter(lambda x: x.isupper(), text))
print(upper)

# 25. Write a lambda that returns the square if number is even, cube if odd.

func = lambda x: x**2 if x % 2 == 0 else x**3

print(func(4))  
print(func(3))  

# 26. Use lambda with map to convert Celsius to Fahrenheit.

cel = [0, 20, 30, 40]

fr = list(map(lambda c: (c * 9/5) + 32, cel))
print(fr)

# 27. Write a lambda to check if two strings are anagrams.

anagram = lambda s1, s2: sorted(s1) == sorted(s2)

print(anagram("listen", "silent"))

# 28. Use lambda to extract only numeric values from a mixed list.

l1 = [10, "hi", 3.5, "hello", 7]

numbers = list(filter(lambda x: isinstance(x, (int, float)), l1))
print(numbers)

# 29. Use lambda inside any() to check if any list element is negative.


nums = [5, 8, -2, 10]

negative = any(map(lambda x: x < 0, nums))

print(negative)

# 30. Use lambda to generate a function that multiplies any number by n

mul = lambda n: lambda x: x * n

times3 = mul(3)
print(times3(10))   # 30