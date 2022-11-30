class Vehicle:
    
    def __init__(self, name, color, num_wheels, speed): #each object has a self to identify it 
        self.name = name #take perameters and assign them a value
        self.color = color
        self.num_wheels = num_wheels
        self.speed = speed 


bug_object = Vehicle("beetle", "yellow", 4, 1) #object(or instance) of vehicle class
turtle = Vehicle("turtlebot", "green", 2, 5) #turtle is also an object, don't need to say object for it to be an object
rover = Vehicle("rover", "purple", 4, 25) #third object

print(bug_object) #can callout where object is in mempory, or callout for value of 
print(turtle.color) #can callout value of an attribute
print('This vehicle is', rover.color, 'with', rover.num_wheels, 'wheels, and can drive', rover.speed, 'mph.')