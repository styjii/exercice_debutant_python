# fonction de base
# trier trois nombre sans condition ou sort

a = 4
b = 6
c = 2

# d = a
# a = c
# c = b
# b = d

# print(f"Les nombres dans l'ordre sont {a}, {b} et {c}")


a1 = min(a, b, c)
c1 = max(a, b, c)
b1 = (a + b + c) - a1 - c1

print(f"Les nombres dans l'ordre sont {a1}, {b1} et {c1}")