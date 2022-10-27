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

def print_options():
  print()
  choice = input("[e]xplore [i]nventory [p]layer [w]ait [q]uit> ").lower()
  if choice == "e":
    render.display_map()
    return
  elif choice == "i":
    pass
  elif choice == "p":
    player.print_player_stats()
  elif choice == "w":
    pass
  elif choice == "q":
    quit()