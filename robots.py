#import all classes
from weapons import Weapons


#region - initializ robots class and set methods

#robots class
class Robots:
    #robot properties
    def __init__(self, name, weapon):
        self.name = name
        self.health = 100
        self.weapon = weapon.weapon_name
        self.attack_power = weapon.attack_power


#endregion