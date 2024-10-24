"""Tuple dagi elementlarni teskari qilib chiqaring."""

letters = ("a", "b", "c", "d", "e")
letters = list(letters)
letters.reverse()
letters = tuple(letters)

print(letters)