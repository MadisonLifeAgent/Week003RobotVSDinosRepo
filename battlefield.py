#instantiate robots, dinosaurs, weapons, fleets, and herds

#region - import all classes
from fleet import Fleet
from herd import Herd
from matches import Matches


#endregion

#region - instantiate fleet which has robots and weapons
robot_fleet = Fleet()
robot_fleet.set_robot_fleet()

# print fleet names (debugging)
#use this format to get attributes from
#print(robot_fleet.name[1].name)
#print(robot_fleet.name[1].health)
#print(robot_fleet.name[1].weapon)
#print(robot_fleet.name[1].attack_power)

#endregion - instantiate fleet which has robots and weapons

#region - instantiate heard

dino_herd = Herd()
dino_herd.set_herd()

#endregion - instantiate heard

#region - assign apponents
#Match One - robot one and dino one
begin_the_battle = Matches(robot_fleet, dino_herd)
begin_the_battle.fight_to_the_death()

#endregion - assign opponends end

