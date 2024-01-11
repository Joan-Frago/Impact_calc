class Object:

    def __init__(self, mass, vo):
        self.mass = mass # peso
        self.vo = vo # velocidad inicial

    def object_info(self):
        return "\nMass: {}    Initial vel: {}   Initial pos: {}".format(self.mass, self.vo, self.xo)

def final_vel(mass1,mass2,vo1,vo2):

    # CONSERVACIÓN MOMENTO LINEAL
    # m1*vo1 + m2*vo2 = m1*v1 + m2*v2

    # CONSERVACIÓN DE LA ENERGÍA CINÉTICA
    # m1*(vo1**2) + m2*(vo2**2) = m1*(v1**2) + m2*(v2**2)

    # bucle --> cada iteración --> calcular velocidades + invertir signo v2 + sumar al contador de impactos
    impact_counter = 1
    
    v1 = (((mass1 - mass2) / (mass1 + mass2)) * vo1) + (((2*mass2) / (mass1 + mass2)) * vo2)
    print(f"v1: {v1}")

    v2 = (((2*mass1) / (mass1 + mass2)) * vo1) + (((mass2 - mass1) / (mass1 + mass2)) * vo2)
    print(f"v2: {v2}")

    while v2 < 0 or v2 > v1:
        v2 = v2 * -1
        v1 = (((mass1 - mass2) / (mass1 + mass2)) * v1) + (((2*mass2) / (mass1 + mass2)) * v2)
        print(f"v1: {v1}")
        v2 = (((2*mass1) / (mass1 + mass2)) * v1) + (((mass2 - mass1) / (mass1 + mass2)) * v2)
        print(f"v2: {v2}")
        impact_counter += 1
    
    print(impact_counter)


def main():
    Object1 = Object(1, -5) # mass, initial vel
    Object2 = Object(1, 0) # mass, initial vel
    
    mass1 = Object1.mass
    mass2 = Object2.mass
    vo1 = Object1.vo
    vo2 = Object2.vo

    final_vel(mass1,mass2,vo1,vo2)

main()