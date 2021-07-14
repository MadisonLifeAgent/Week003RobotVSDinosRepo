#instantiate robots, dinosaurs, weapons, fleets, and herds

#region - import all classes
# import weapons so robots have weapons
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd

#endregion

#region - call robot weapons
sword_weapon = Weapons("Sword", 10)
liquid_metal = Weapons("Liquid Metal", 5)
dew = Weapons("Direct Energy Weapon", 20)

#endregion

#region - call robots
robot_one = Robots("Gundam", sword_weapon)
robot_two = Robots("T1000", liquid_metal)
robot_three = Robots("Sentinels", dew)

#endregion

#region - 

#region - debug lines
print(robot_three.name)
print(robot_three.health)
print(robot_three.weapon)
print(robot_three.attack_power)
#endregion - debug lines