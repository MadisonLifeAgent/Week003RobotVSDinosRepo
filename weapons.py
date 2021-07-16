# Weapons Class that will be instantiated for use by fleet, robots, and battlefield

#region - initializ weapons class and set methods
class Weapons:
    #weapons properties/attributes
    def __init__(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power


    #set methods to get weapons (this area not in use)
    def set_weapon(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power

#endregion