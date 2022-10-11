# constant list of genders
GENDERS = ["male", "female", "non-binary"]

class Player:
    genders = ["male".lower(), "female".lower(), "non-binary".lower()]
    max_hp = 100
    def __init__(self, name, gender, max_hp):
        self.name = name
        self.gender = gender
        self.max_hp = max_hp

    def validate_input(self, input, list):
        if input not in list or input == "":
            return "Invalid input, tay "
        return None

    def get_gender(self):
        chosen_gender = input("Are you male, female or non-binary?: ").lower()

        if chosen_gender not in Player.genders or chosen_gender == "":
            return "Invalid input, Please type: male, female or non-binary: "
        return None

def validate_name(name):
    """determines if the passed name is not empty
    
    returns a boolean"""
   
    return name != ""
