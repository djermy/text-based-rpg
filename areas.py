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
    "base": Locations("Base", "Your base at the outskirts of the forest. There isn't much to it as you set it up in a hurry, but the little you have is organized into piles. you have your bedroll set up in a small tent, under a small tree to help protect against the rain. Inside your tent you store the few clothes and posessions you own. Looking in the direction your tent is facing, is the forest, from here you can just make out the entrance."),
    "forest": Locations("Forest", "The forest feels a lot bigger now you're inside compared to viewing it from your camp. The forest floor is littered with decaying twigs, branches, leaves, and other vegetation, acting as a thick mulch, preventing many smaller plants growing along the main paths. You see rays of light gently filtering through the thick canopy of the forest. You hear the birds chirping, bugs buzzing and other forest critters scampering around, You figure there must be water and more vegetation inside feeding all the wildlife you hear around you."),
    "mountains": Locations("Mountains", "You tread carefully along the rocky paths of the mountains, being careful not to fall over the edge at times or slip and hit your head against the fallen boulders. Ocassionally you hear birds, the fearce whistling winds, and narrowly avoid the rare piece of falling stone from the rockfaces overhead."),
    "town": Locations("Town", "As you walk into town, you hear the hustle and bustle of the townsfolk going about their business. Furhter towards the town center is the marketplace. The marketplace is filled with market stalls selling all sorts of goods, along with the towns church, library, water fountain and the odd shop"),
}