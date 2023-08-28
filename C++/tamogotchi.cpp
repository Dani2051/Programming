#include <iostream>
#include <string>
#include <thread>
#include <chrono>
using namespace std;

class Cat {
  private:
    string name;
    double age = 1; 
    double health = 100;
    double hunger = 100;
    double happiness = 100;
    double fatigue = 0;
    double cleanliness = 100;

  public:
    Cat(string pName) {
      name = pName;
      cout << "You have adopted a new cat called " << name << endl;
    }

    bool state() {
      if (health > 0) {
        return true;
      } else {
        return false;
      }
    }

    double getHealth() {
      return health;
    }

    double getHunger() {
      return hunger;
    }

    double getFatigue() {
      return fatigue;
    }

    void changeHealth(double value) {
      health += value;
    }

    void changeHunger(double value) {
      hunger += value;
    }

    void changeFatigue(double value) {
      fatigue += value;
    }
};

int main() {
  string name;
  cout << "What would you like to name your cat? ";
  cin >> name;

  Cat c1(name);

  int day = 1;
  while (c1.getHealth() >= 0) {
    cout << "Day " << day << endl;
    cout << "Health: " << c1.getHealth() << endl;
    cout << "Hunger: " << c1.getHunger() << endl;
    cout << "Fatigue: " << c1.getFatigue() << endl;
    cout << "--------------------------------" << endl;
    day++;

    c1.changeHealth(-0.4);
    c1.changeHunger(-2.6);
    c1.changeFatigue(1.5);

    this_thread::sleep_for(chrono::milliseconds(1000) );
  }

  //cout << "dead";
  return 0;
}