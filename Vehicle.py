class Vehicle:
    pass

bug_object = Vehicle() #object(or instance) of vehicle class
turtle = Vehicle() #turtle is also an object, don't need to say object for it to be an object
rover = Vehicle() #third object

bug_object.color = "yellow" #object(or instance) of vehicle class and attribute
bug_object.num_wheels = 4
bug_object.speed = 1

turtle.color = "green" 
turtle.num_wheels = 2
turtle.speed = 5

rover.color = "purple"
rover.num_wheels = 4
rover.speed = 25

print(bug_object) #can callout where object is in mempory, or callout for value of 
print(turtle.color) #can callout value of an attribute
print('This vehicle is', rover.color, 'with', rover.num_wheels, 'wheels, and can drive', rover.speed, 'mph.')