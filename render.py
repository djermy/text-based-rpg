import math
import areas
import util

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

def print_inventory(inventory):
  for item in inventory:
    print(item)
  print()
  input("[next]")

def print_options(player):
  print()
  choice = input("[e]xplore [i]nventory [p]layer [r]est [q]uit> ").lower()
  if choice == "e":
    util.clear_screen()
    display_map()
    input("[next]")
    return
  elif choice == "i":
    util.clear_screen()
    print("You have:")
    print_inventory(player.inventory)
  elif choice == "p":
    util.clear_screen()
    player.print_player_stats()
  elif choice == "r":
    print("You sit and rest for a few hours.\nYou recover you're fatigue")
    player.rest()
  elif choice == "q":
    quit()
  
def display_map():
    list_of_areas = [i.upper() for i in areas.game_map.keys()]
    count = 1
    for area in list_of_areas:
      print("[" + str(count) + "]" + ". " + area + "\n")
      count += 1
    choice = input("Where to?> ")
    if int(choice) > len(list_of_areas):
      print("Invalid selection, please try again")
      return display_map()
    else:
      areas.game_map[list_of_areas[int(choice)-1].lower()].print_description()