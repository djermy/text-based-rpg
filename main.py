import rpg
import util
import areas
import render

def main():
    # state
    name = util.user_input_name()
    gender = util.user_input_gender()
    
    # instantiate object
    player = rpg.Player(name, gender, 10, rpg.Player.max_hp, 100, 0, 0, 5, 5, 5)
    player.inventory.append("bucket")
    player.inventory.append("potion")
    
    while True:
        areas.game_map["base"].print_description()
        render.print_options(player)

if __name__ == "__main__":
    main()