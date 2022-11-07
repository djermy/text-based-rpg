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

    # render
    render.display_map()
    areas.game_map["base"].print_description()
    player.display_player_bar()
    player.print_player_stats()
if __name__ == "__main__":
    main()