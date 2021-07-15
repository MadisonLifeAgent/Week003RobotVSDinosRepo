#instantiate robots, dinosaurs, weapons, fleets

#region - import weapons and robots classes
from weapons import Weapons
from robots import Robots

#endregion

#region - initializ fleet class and set methods
#fleet class
class Fleet:
    #fleet properties
    def __init__(self):
        self.names = [] # get from objects
        self.lives = 3 # one life for each robot in the fleet

    # set fleet to be instantitated
    def set_robot_fleet(self):
        self.names.append(robot_one)
        self.names.append(robot_two)
        self.names.append(robot_three)
        

#endregion

#region - instantiate robots and weapons
liquid_metal = Weapons("Liquid Metal", 5)
dew = Weapons("Direct Energy Weapon", 10)
sword_weapon = Weapons("Sword", 20)

robot_one = Robots("T1000", liquid_metal)
robot_two = Robots("Sentinel", dew)
robot_three = Robots("Mobile Suit Gundam Wing", sword_weapon)

#endregion

#region - debug lines
#print robot names
#print(robot_three.name)
#print(robot_three.health)
#print(robot_three.weapon)
#print(robot_three.attack_power)

# print fleet names

#print(robot_list[0].name)
#print(robot_list[0].health)
#print(robot_list[0].weapon)
#print(robot_list[0].attack_power)

#endregion - debug lines