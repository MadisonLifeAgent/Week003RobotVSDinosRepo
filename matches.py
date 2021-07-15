#region - import all classes
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs

#endregion

#region - create matches class
class Matches:
    def __init__(self, robot_name, robot_health, dino_name, dino_health):
        self.robot_name = robot_name
        self.robot_health = robot_health
        self.dino_name = dino_name
        self.dino_health = dino_health
        self.whos_turn = bool

    #decide who's turn it is to attack
    def fight_to_the_death(self):
        if (self.robot_health == self.dino_health):
            #dinosaur attack
            self.dino_health -= 10
            print(self.dino_health)


#endregion - class