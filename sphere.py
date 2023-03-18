import math
x = float(input())
print(round((3/4 * math.pi * x**3 - x**3 + math.sin(x)**3) % 1, 2))