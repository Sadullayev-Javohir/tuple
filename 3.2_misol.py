"""Quyidagi tuple ni yarating: colors = ("red", "green", "blue") uni ro'yxatga aylantiring va unga yangi element
qo'shing: "yellow" """

colors = ("red", "green", "blue")

colors = list(colors)
colors.append("yellow")
colors = tuple(colors)

print(colors)