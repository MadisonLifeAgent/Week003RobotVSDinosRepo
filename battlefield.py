#instantiate robots, dinosaurs, weapons, fleets, and herds

#region - import all classes
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd

#endregion

#region - instantiate robot weapons
sword_weapon = Weapons("Sword", 10)
liquid_metal = Weapons("Liquid Metal", 5)
dew = Weapons("Direct Energy Weapon", 20)

#endregion

#region - instantiate robots
robot_one = Robots("Mobile Suit Gundam Wing", sword_weapon)
robot_two = Robots("T1000", liquid_metal)
robot_three = Robots("Sentinel", dew)

#endregion

#region - instantiate fleet and put robots in fleet
robot_list = []
robot_list.append(robot_one)
robot_list.append(robot_two)
robot_list.append(robot_three)

#endregion

#region - debug lines
# print robot names
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