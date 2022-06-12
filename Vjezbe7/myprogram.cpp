#include "Particle.cpp"
#include <iostream>

int main(){
    Particle p1(10, 0.1, 0, 0);
    std::cout << "Domet cestice je: " << p1.range() << std::endl;
    std::cout << "Vrijeme leta cestice je: " << p1.time() << std::endl;

    Particle p2(3, 0.7, 2, 2);
    std::cout << "Domet cestice je: " << p2.range() << std::endl;
    std::cout << "Vrijeme leta cestice je: " << p2.time()<< std::endl;
    return 0;
};