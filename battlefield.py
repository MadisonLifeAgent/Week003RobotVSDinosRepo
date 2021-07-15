#instantiate robots, dinosaurs, weapons, fleets, and herds

#region - import all classes
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs
from fleet import Fleet
from herd import Herd

#endregion

#region - instantiate fleet which has robots and weapons
robot_fleet = Fleet()
robot_fleet.set_robot_fleet()

# print fleet names (debugging)
#use this format to get attributes from
print(robot_fleet.names[1].name)
print(robot_fleet.names[1].health)
print(robot_fleet.names[1].weapon)
print(robot_fleet.names[1].attack_power)

#endregion - instantiate fleet which has robots and weapons

#region - instantiate heard

dino_herd = Herd()
dino_herd.set_herd()

# print fleet names (debugging)
#use this format to get attributes from
print("\nVS.\n")
print(dino_herd.names[1].name)
print(dino_herd.names[1].health)
print(dino_herd.names[1].attack_power)

#endregion - instantiate heard