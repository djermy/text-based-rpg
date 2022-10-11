import rpg
import render

def main():

# get user name
    user_input = input("What is your name?: ")

    # get gender
    gender = rpg.Player.get_gender()

    # instantiate object
    player = rpg.Player(user_input, gender, rpg.Player.max_hp)

if __name__ == "__main__":
    main()

