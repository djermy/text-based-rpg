import math

def print_bar(val, max):
    size = 20
    if val < 0:
      val = 0
    if val > max:
      val = max
    ratio = val / max
    how_many_equals = ratio * size
    num = math.floor(how_many_equals)
    print("[", end="")
    for i in range(num):
      print("=", end="")
    for i in range(size - num):
      print(" ", end="")
    print("]", end="")