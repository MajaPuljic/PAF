#include <iostream>

void sustav_jednadzbi(float a1, float b1, float c1, float a2, float b2, float c2){
    float k1 = a1/a2;
    float b = b1 - k1*b2;
    float c = c1 - k1*c2;
    float y = c/b;
    float x = (c1 - b1*y)/a1;
    std::cout << "x: " << x << "\n y: " << y <<std::endl;
};

int main(){
    sustav_jednadzbi(5,3,1,2,6,7);
    return 0;
};