#Dinosaurs Class
#region - initialize dinosaur class and set methods

#dinosaur class and attributes/properties
class Dinosaurs:
    def __init__(self, name, attack):
        self.name = name
        self.health = 100
        self.attack_power = attack
    
    #set got attacked method (loses health based on robot weapon attack power)
    def dino_attacked(self, name, attack):
        self.health -= attack 
        return name

#endregion