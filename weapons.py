#region - initializ weapons class and set methods

#weapons class
class Weapons:
    #weapons properties
    def __init__(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power

#endregion

#region - set methods to get weapons
    def set_weapon(self, weapon_name, attack_power):
        self.weapon_name = weapon_name
        self.attack_power = attack_power

#endregion