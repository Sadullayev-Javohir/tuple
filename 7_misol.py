"""Ikkita tuple ni birlashtirib yangi tuple hosil qiling."""

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

tuple1, tuple2 = list(tuple1), list(tuple2)
tuple1.extend(tuple2)
tuple1 = tuple(tuple1)

print(tuple1)