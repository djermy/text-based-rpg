import rpg
import render
import util

def main():
    # state
    name = util.user_input_name()
    gender = util.user_input_gender()
    # instantiate object
    player = rpg.Player(name, gender, rpg.Player.max_hp)

if __name__ == "__main__":
    main()
