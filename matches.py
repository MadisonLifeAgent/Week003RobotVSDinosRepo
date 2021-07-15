#region - import all classes
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs

#endregion

#region - create matches class
class Matches:
    def __init__(self, fleet, herd):
        self.fleet = fleet
        self.herd = herd
        self.whos_turn = bool

    #decide who's turn it is to attack
    def fight_to_the_death(self):
        #print fight details
        print("Match 1\n" + self.fleet.name[0].name + " VS. " + self.herd.name[0].name)
        while (self.fleet.lives > 0 or self.herd.lives > 0):
            if (self.fleet.name[0].health == self.herd.name[0].health):
            #robot/fleet attack
                self.herd.name[0].health -= 10
                print(self.herd.name[0].health)
            #dino/herd attack
            elif (self.fleet.name[0].health > self.herd.name[0].health):
                self.fleet.name[0].health -= 10
                print(self.fleet.name[0].health)

#endregion - class