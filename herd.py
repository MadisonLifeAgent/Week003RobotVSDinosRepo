#import dinosaurs
from dinosaurs import Dinosaurs

#region - initializ herd class and set methods
from dinosaurs import Dinosaurs
from matches import Matches

#herd class
class Herd:
    #herd properties
    def __init__(self):
        self.name = []
        self.lives = 3

    #set herd to be instantiated
    def set_herd(self):
        self.name.append(dino_one)
        self.name.append(dino_two)
        self.name.append(dino_three)

#endregion

#instantiate dinosaurs
dino_one = Dinosaurs("Velociraptor", 5)
dino_two = Dinosaurs("Utahraptor", 10)
dino_three = Dinosaurs("T-Rex", 20)
