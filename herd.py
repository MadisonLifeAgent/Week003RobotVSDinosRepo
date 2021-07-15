#import dinosaurs
from dinosaurs import Dinosaurs

#region - initializ herd class and set methods

#herd class
class Herd:
    #herd properties
    def __init__(self):
        self.names = [] # get from objects
        self.lives = 3 # one life for each dinosaur in the herd

    #set herd to be instantiated
    def set_herd(self):
        self.names.append(dino_one)
        self.names.append(dino_two)
        self.names.append(dino_three)

#endregion

#instantiate dinosaurs
dino_one = Dinosaurs("Velociraptor", 5)
dino_two = Dinosaurs("Utahraptor", 10)
dino_three = Dinosaurs("T-Rex", 20)
