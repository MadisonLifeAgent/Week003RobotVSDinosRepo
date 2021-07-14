#instantiate robots, dinosaurs, weapons, fleets, and herds

#region - import all classes
# import weapons so robots have weapons
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd

#endregion

#region - call weapons
sword_weapon = Weapons("Sword", 10)
print(sword_weapon.weapon_name)
print(sword_weapon.attack_power)

#endregion

#region - call robots
robot_one = Robots("Gundam", sword_weapon)
print(robot_one.name)
print(robot_one.health)
print(robot_one.weapon)
print(robot_one.attack_power)

#endregion