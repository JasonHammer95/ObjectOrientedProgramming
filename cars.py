# import
from Vehicle import Vehicle

bug_object = Vehicle("beetle", "yellow", 4, 1) #object(or instance) of vehicle class
turtle = Vehicle("turtlebot", "green", 2, 5) #turtle is also an object, don't need to say object for it to be an object
rover = Vehicle("rover", "purple", 4, 25) #third object

bug_object.print_details()
turtle.print_details()
rover.print_details()

bug_object.paint_vehicle("blue")

bug_object.print_details()