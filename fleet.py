#Fleet Class - that will instantitate robots and weapons

#region - import weapons and robots classes
from weapons import Weapons
from robots import Robots

#endregion

#region - initializ fleet class and set methods
#fleet attributes/properties
class Fleet:
    def __init__(self):
        self.name = []
        #self.lives = 3

    # set method so fleet can be instantitated
    def set_robot_fleet(self):
        self.name.append(robot_one)
        self.name.append(robot_two)
        self.name.append(robot_three)

#endregion

#region - instantiate robots and weapons
#weapons
liquid_metal = Weapons("Liquid Metal", 5)
dew = Weapons("Direct Energy Weapon", 10)
sword_weapon = Weapons("Sword", 20)

#robots
robot_one = Robots("T1000", liquid_metal)
robot_two = Robots("Sentinel", dew)
robot_three = Robots("Mobile Suit Gundam Wing", sword_weapon)

#endregion