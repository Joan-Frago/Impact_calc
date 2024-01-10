class Object:

    def __init__(self, mass, v, vo, xo, t, to):
        self.mass = mass # peso
        self.v = v # velocidad final
        self.vo = vo # velocidad inicial
        self.xo = xo # posición inicial
        self.t = t # tiempo final
        self.to = to # tiempo inicial

    def object_info(self):
        return "\nMass: {}    Initial vel: {}   Initial pos: {}".format(self.mass, self.vo, self.xo)

def final_vel(mass1,mass2,v1,v2,vo1,vo2):

    # CONSERVACIÓN MOMENTO LINEAL
    # m1*vo1 + m2*vo2 = m1*v1 + m2*v2

    # CONSERVACIÓN DE LA ENERGÍA CINÉTICA
    # m1*(vo1**2) + m2*(vo2**2) = m1*(v1**2) + m2*(v2**2)

    # operaciones funcionan
    
    v1 = (((mass1 - mass2) / (mass1 + mass2)) * vo1) + (((2*mass2) / (mass1 + mass2)) * vo2)
    print(f"v1: {v1}")

    v2 = (((2*mass1) / (mass1 + mass2)) * vo1) + (((mass2 - mass1) / (mass1 + mass2)) * vo2)
    print(f"v2: {v2}")

def position(xo1, xo2, v1, v2, t1, t2, to1, to2):
    
	# x = xo + v * t
    
	x1 = 0
    
	x2 = xo1

    # x1 = xo1 + v1 * (t1 - to1)
    # x2 = xo2 + v2 * (t2 - to2)

def main():
    Object1 = Object(10, 0, -5, 5, 0, 0) # mass, initial vel, pos inicial
    Object2 = Object(1, 0, 0, 10, 0, 0) # mass, initial vel, pos inicial
    
    mass1 = Object1.mass
    mass2 = Object2.mass
    v1 = Object1.v
    v2 = Object2.v
    vo1 = Object1.vo
    vo2 = Object2.vo
    xo1 = Object1.xo
    xo2 = Object2.xo
    t1 = Object1.t
    t2 = Object2.t
    to1 = Object1.to
    to2 = Object2.to

    final_vel(mass1,mass2,v1,v2,vo1,vo2)
    position(xo1,xo2,v1,v2,t1,t2,to1,to2)

main()