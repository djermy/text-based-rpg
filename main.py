import rpg
import util
import areas
import render

def main():
    # state
    util.clear_screen()
    name = util.user_input_name()
    util.clear_screen()
    gender = util.user_input_gender()
    util.clear_screen()

    # instantiate object
    player = rpg.Player(name, gender, 10, rpg.Player.max_hp, 100, 50, 0, 5, 5, 5)
    player.inventory.append("bucket")
    player.inventory.append("potion")
    
    while True:
        util.clear_screen()
        areas.game_map["base"].print_description()
        render.print_options(player)

if __name__ == "__main__":
    main()