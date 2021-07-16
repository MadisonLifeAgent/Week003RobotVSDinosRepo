#region - import all classes
from fleet import Fleet
from herd import Herd
from dinosaurs import Dinosaurs

#instantiate robots, dinosaurs, weapons, fleets, and herds
class Battlefield:
    def __init__(self):
        self.start_battle = True
        self.end_battle = False
        self.robot_lives = 0
        self.dino_lives = 0


    def begin_battle(self):
        self.start_battle = True

    def fights(self):
        while self.start_battle == True:
            if (self.robot_lives > 2):
                self.start_battle = False
                print("Dinosaurs Win!\n")
                break

            elif (self.dino_lives > 2):
                self.start_battle = False
                print("Robots Win!\n")
                break
            
            #if no winner yet, keep the battle going
            #set index value
            index_number = self.dino_lives

            while robot_fleet.name[index_number].health >= 0 or dino_herd.name[index_number].health != 0:

                #if both health are equal robot attacks
                if(robot_fleet.name[index_number].health == dino_herd.name[index_number].health):

                    #instantiate a robot attack (dino actually loses health, so the instance is in the dinosaur class)
                    dino_herd.name[index_number].dino_attacked(dino_herd.name[index_number].name,robot_fleet.name[index_number].attack_power)

                # if robot health is higher, dino attacks
                elif(robot_fleet.name[index_number].health > dino_herd.name[index_number].health and dino_herd.name[index_number].health > 0):
                    
                    #instantiate a robot attack (dino actually loses health, so the instance is in the dinosaur class)
                    robot_fleet.name[index_number].robot_attacked(robot_fleet.name[index_number].name,dino_herd.name[index_number].attack_power)

                # if robot health is still above 0, and dino health is <= 0, robot wins
                elif(robot_fleet.name[index_number].health > 0 and dino_herd.name[index_number].health == 0):
                    
                    #Display message stating Robot won
                    print(robot_fleet.name[index_number].name + " defeats " + dino_herd.name[index_number].name + "\n")

                    #subtract a dinosaur life since they loss
                    self.dino_lives += 1

                    #end the loop since the fight is over
                    break

                elif(robot_fleet.name[index_number].health == 0 and dino_herd.name[index_number].health > 0):
                    
                    #display message stating dinosaur won
                    print(dino_herd.name[index_number].name + " defeats " + robot_fleet.name[index_number].name + "\n")

                    #subtract a robot fleet life since they loss
                    self.robot_lives += 1

                    #end the loop since the fight is over
                    break
                
#endregion

#region - instantiate fleet which has robots and weapons
robot_fleet = Fleet()
robot_fleet.set_robot_fleet()

#endregion - instantiate fleet which has robots and weapons

#region - instantiate herd

dino_herd = Herd()
dino_herd.set_herd()

#endregion - instantiate heard