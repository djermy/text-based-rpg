import rpg
import util

def main():
    # state
    name = util.user_input_name()
    gender = util.user_input_gender()

    # instantiate object
    player = rpg.Player(name, gender, rpg.Player.max_hp, 100, 0, 0, 5, 5, 5)

if __name__ == "__main__":
    main()