class Object:

    def __init__(self, mass, initial_velocity, final_velocity):
        self.mass = mass
        self.initial_velocity = initial_velocity
        self.final_velocity = final_velocity

    def object_info(self):
        return "Mass: {}    Initial vel: {}     Final vel: {}".format(self.mass,self.initial_velocity,self.final_velocity)

Object1 = Object(float(input("Mass 1: ")), float(input("Initial vel 1: ")), float(input("Final vel 1: ")))
Object2 = Object(float(input("Mass 2: ")), float(input("Initial vel 2: ")), float(input("Final vel 2: ")))

