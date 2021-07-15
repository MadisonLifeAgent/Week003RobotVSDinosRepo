#instantiate robots, dinosaurs, weapons, fleets

#region - import all classes
from weapons import Weapons
from robots import Robots
from dinosaurs import Dinosaurs

#endregion

#region - initializ fleet class and set methods

#fleet class
class Fleet:
    #fleet properties
    def __init__(self):
        self.names = [] # get from objects
        self.lives = 3 # one life for each robot in the fleet

#endregion