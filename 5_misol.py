"""Ichkaridagi tuple dagi ikkinchi elementni chiqaring. Tuple dagi barcha elementlarni chiqaradigan sikl yozing."""

nested_tuple = (1, 2, (3, 4, 5), 6, 7)

nested_tuple = list(nested_tuple)

print(nested_tuple[2])