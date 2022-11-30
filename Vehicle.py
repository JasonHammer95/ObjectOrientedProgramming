class Vehicle:

    #class level attribute
    type = "ground"
    propulsion = "battery"
    
    def __init__(self, name, color, num_wheels, speed): #each object has a self to identify it 
        self.name = name #take perameters and assign them a value
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed 

    def print_details(self):
        print(self.name, 'is', self.color, 'and is able to drive', self.speed, 'mph')
    
    def paint_vehicle(self, newcolor):
        self.color = newcolor