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
        #self.whos_turn = bool

    #decide who's turn it is to attack
    def fight_to_the_death(self):
        # use counter to end looping
        counter = 0

        while counter < 3:
            
            #check health of robots or dinosaurs
            while self.fleet.name[counter].health != 0 and self.herd.name[counter].health != 0:

                # determine who attacks first
                #robot/fleet attack
                if (self.fleet.name[counter].health == self.herd.name[counter].health):
                    self.herd.name[counter].health -= self.fleet.name[counter].attack_power
                    print(self.herd.name[counter].health)

                #dino/herd attack
                elif (self.fleet.name[counter].health > self.herd.name[counter].health):
                    self.fleet.name[counter].health -= self.herd.name[counter].attack_power
                    print(self.fleet.name[counter].health)

            #determine if a creature has loss
            if (self.fleet.lives != 0 or self.herd.lives != 0):
                #subtract a robot from the fleet
                if (self.fleet.name[counter].health == 0):
                    self.fleet.lives -= 1
                    print(self.fleet.lives)
                    print("Dinosaurs win this match")
                    counter -= 1

                #subtract a dinosaur from the fleet
                elif (self.herd.name[counter].health == 0):
                    self.herd.lives -= 1
                    print(self.herd.lives)
                    print("Robots win this match")
                    counter -= 1

            #determine who won the battle
            if (self.fleet.lives == 0):
                print("Dinosaurs win the battle!")
                break
            elif (self.herd.lives == 0):
                print("Robots win the battle!")
                break

#endregion - class