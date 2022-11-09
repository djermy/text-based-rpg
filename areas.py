class Locations:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "[{name}]".format(name=self.name)
    
    def print_description(self):
        print()
        print(self.name)
        print()
        print(self.description)
        print()

game_map = {
    "base": Locations("Base", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>"),
    "forest": Locations("Forest", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>"),
    "mountains": Locations("Mountains", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>"),
    "town": Locations("Town", "<PLACEHOLDER DESCRIPTION, REMOVE AND REPLACE>"),
}