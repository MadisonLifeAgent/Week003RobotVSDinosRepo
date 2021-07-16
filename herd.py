#Herd Class - Instantiates dinosaurs into a list for use in battlefield

#region - initializ herd class and set methods
#import dinosaurs
from dinosaurs import Dinosaurs

#herd class and attributes/properties
class Herd:
    def __init__(self):
        self.name = []
        self.lives = 3

    #set method so herd can be instantiated
    def set_herd(self):
        self.name.append(dino_one)
        self.name.append(dino_two)
        self.name.append(dino_three)

#endregion

#instantiate dinosaurs so they can be used in battlefield
dino_one = Dinosaurs("Velociraptor", 5)
dino_two = Dinosaurs("Utahraptor", 10)
dino_three = Dinosaurs("T-Rex", 20)
