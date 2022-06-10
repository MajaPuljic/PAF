#include <iostream>
#include <sstream>  
#include <list>
using namespace std;

void sustav(float a1,float b1, float c1, float a2, float b2, float c2){
    float x;
    float y;
    if((a1*b2 - b1*a2) != 0){
        x = (c1*b2 - b1*c2)/(a1*b2 - b1*a2);
        y = (a1*c2 - c1*a2)/(a1*b2 - b1*a2);
        std::cout << "(" << x << "," << y << ")";
    }
    else{
        std::cout << "Jednadzba nema rijesenja.";
    }
    
}

int main(){

    sustav(2, 3, 2, 2, 3, 7);

    return 0;
}
