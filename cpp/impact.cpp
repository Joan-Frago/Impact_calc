# include <iostream>
# include <string>
# include <stdexcept>

class Square {
  public:
  std::string SquareInfo(float mass, float init_vel) {
    std::string str = "";
    try {
      str += "\n";
      str += "    Mass: " + std::to_string(mass) + "\n";
      str += "    Initial vel: " + std::to_string(init_vel) + "\n";
    }
    catch (const std::exception& e) {
      std::cout << "Exception " << e.what() << std::endl;
    }

    return str;
  }
};

void Welcome() {
  try {
    std::string message = "WELCOME TO THE IMPACT CALCULATION APP";
    std::cout << std::endl << message << std::endl << std::endl;
  }
  catch (const std::exception& e) {
    std::cout << "Exception " << e.what() << std::endl;
  }
}

int getChoice() {
    int choice;
  try {
    std::cout << "Choose an option:" << std::endl;
    std::cout << "  --> 1. Set mass" << std::endl;
    std::cout << "  --> 2. Run program" << std::endl;
    std::cout << "  --> 3. Exit program" << std::endl;
    std::cout << std::endl << "  --> ";
    std::cin >> choice;

    return choice;
  }
  catch (const std::exception& e) {
    std::cout << "Exception " << e.what() << std::endl;
  }
}

int ImpactCalc(int mass1,int mass2,int vo1,int vo2) {
  int impact_counter = 0;
  std::cout << "Starting impact calculation..." << std::endl;
  try {
    std::cout << "Started impact calculation:" << std::endl;
    // CONSERVACIÓN MOMENTO LINEAL
    // m1*vo1 + m2*vo2 = m1*v1 + m2*v2
    //
    // CONSERVACIÓN DE LA ENERGÍA CINÉTICA
    // m1*(vo1**2) + m2*(vo2**2) = m1*(v1**2) + m2*(v2**2)
    //
    // bucle --> cada iteración --> calcular velocidades + invertir signo v2 + sumar al contador de impactos

    impact_counter = 1;

    // Calculate v1
    float v1 = (((mass1 - mass2) / (mass1 + mass2)) * vo1) + (((2*mass2) / (mass1 + mass2)) * vo2);
    std::cout << "v1: " << v1 << std::endl;
    // Calculate v2
    float v2 = (((2*mass1) / (mass1 + mass2)) * vo1) + (((mass2 - mass1) / (mass1 + mass2)) * vo2);
    std::cout << "v2: " << v2 << std::endl;
    // print current number of impacts
    std::cout << "Number of impacts: " << impact_counter << std::endl;

    while (v2 < 0 || v2 > v1) {
      std::cout << std::endl;
      // Reverse vel because of impact
      v2 = v2 * -1;
      // Add an impact
      impact_counter ++;
      // print current number of impacts
      std::cout << "Number of impacts: " << impact_counter << std::endl;
      // Calculate velocities
      v1 = (((mass1 - mass2) / (mass1 + mass2)) * v1) + (((2*mass2) / (mass1 + mass2)) * v2);
      std::cout << "v1: " << v1 << std::endl;;
      v2 = (((2*mass1) / (mass1 + mass2)) * v1) + (((mass2 - mass1) / (mass1 + mass2)) * v2);
      std::cout << "v2: " << v2 << std::endl << std::endl;
      // Add an impact
      impact_counter ++;
      // print current number of impacts
      std::cout << "Number of impacts: " << impact_counter << std::endl << std::endl;
    }
  }
  catch (const std::exception& e) {
    std::cout << "Exception " << e.what() << std::endl;
  }
  return impact_counter;
}

int main() {
  Welcome();

  int choice = getChoice()

  int num_of_impacts;

  Square square_1;
  float square_1_mass = 10;
  float square_1_init_vel = -5;

  std::string square_1_info = square_1.SquareInfo(square_1_mass,square_1_init_vel);

  Square square_2;
  float square_2_mass = 1;
  float square_2_init_vel = 0;

  std::string square_2_info = square_2.SquareInfo(square_2_mass,square_2_init_vel);

  std::cout << "Square 1 Info:" << square_1_info << std::endl;
  std::cout << "Square 2 Info:" << square_2_info << std::endl;

  num_of_impacts = ImpactCalc(square_1_mass,square_2_mass,square_1_init_vel,square_2_init_vel);

  std::cout << std::endl;
  std::cout << "Total numbers of impacts:";
  std::cout << std::endl << "  --> " << num_of_impacts << std::endl;

  return 0;
}
