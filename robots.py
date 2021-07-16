#import weapons classe
from weapons import Weapons

#region - initialize robots class and set methods
class Robots:
    #robot properties/attributes
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon.weapon_name
        self.attack_power = weapon.attack_power

    #set got attacked method (loses health based on dinosaur attack power)
    def robot_attacked(self, name, attack):
        self.health -= attack 
        return name

#endregion