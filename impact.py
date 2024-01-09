class Object:

    def __init__(self, mass, vo):
        self.mass = mass
        self.vo = vo

    def object_info(self):
        return "\nMass: {}    Initial vel: {}".format(self.mass, self.vo)

def calculate(mass1,mass2,vo1,vo2):

        # CONSERVACIÓN MOMENTO LINEAL
        # m1*vo1 + m2*vo2 = m1*v1 + m2*v2

        # CONSERVACIÓN DE LA ENERGÍA CINÉTICA
        # m1*(vo1**2) + m2*(vo2**2) = m1*(v1**2) + m2*(v2**2)
    
    try:

        # AISLAR V1
        # v1 = (m2*m1*vo1 + (m2**2)*vo2 - m2*vo2 - m1*vo1) / m2*m1 - m1
        v1 = (mass2*mass1*vo1 + (mass2**2)*vo2 - mass2*vo2 - mass1*vo1) / (mass2*mass1 - mass1)
        print(f"v1: {v1}")


        # AISLAR V2
        # v2 = (m1*vo1 + m2*vo2 - m1*v1) / m2
        v2 = (mass1*vo1 + mass2*vo2 - mass1*v1) / mass2
        print(f"v2: {v2}")
        
    except:
        v1 = 0
        v2 = (mass1*vo1 + mass2*vo2 - mass1*v1) / mass2
        print(f"v1: {v1}")
        print(f"v2: {v2}")

def main():
    Object1 = Object(1, -5)
    Object2 = Object(1, 0)
    
    mass1 = Object1.mass
    mass2 = Object2.mass
    vo1 = Object1.vo
    vo2 = Object2.vo

    calculate(mass1,mass2,vo1,vo2)

main()