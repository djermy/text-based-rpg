import math
import os

# constant list of genders
GENDERS = ["male", "female", "non-binary"]
VALID_CHARS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def validate_name(name):
        if name == '':
            return 'No name given, Please try again'

        for i in name:
            if i not in VALID_CHARS.lower():
                return 'You can only enter letters from the latin alphabet.'
        return None

def user_input_name():
    while True:
        name = input("What is your name?: ").strip().lower()
        err = validate_name(name)
        if err != None:
            print(err)
            continue
        else:
            return name

def user_input_gender():
        while True:
            genderKey = input("Select a gender:\n- [M]ale\n- [F]emale\n- [N]on-binary\n\n > ")
            if genderKey == 'M' or genderKey == "m":
                return 'male'
            elif genderKey == 'F' or genderKey == "f":
                return 'female'
            elif genderKey == 'N' or genderKey == "n":
                return 'non-binary'
            else:
                print("Invalid selection")

SCALING = 100
EXPONENT = 1.5
def xp_required_for_level(level):
    return SCALING * math.pow(level, EXPONENT)

def calculate_current_level(xp):
    return math.floor(math.pow(xp / SCALING, 1 / EXPONENT))

def clear_screen():
    return os.system('cls' if os.name == 'nt' else 'clear')

def validate_options_input(options_list, user_input):
    for option in options_list:
        if user_input == option:
            return True
    return False