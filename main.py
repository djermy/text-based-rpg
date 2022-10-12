import rpg
import util

def main():
    # state
    name = util.user_input_name()
    gender = util.user_input_gender()
    base = rpg.Locations("Base", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>")
    forest = rpg.Locations("Forest", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>")
    mountains = rpg.Locations("Mountains", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>")
    town = rpg.Locations("Town", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>")

    # instantiate object
    player = rpg.Player(name, gender, rpg.Player.max_hp, 100, 0, 0, 5, 5, 5)
    print(base)
    base.print_description()

if __name__ == "__main__":
    main()