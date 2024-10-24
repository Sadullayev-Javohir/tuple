"""Tuple dagi birinchi va oxirgi elementlarni chiqaring"""

fruits = ("apple", "banana", "cherry", "orange", "kiwi")

fruits = list(fruits)
pull = fruits[1:4]
pull = tuple(pull)

print(pull)