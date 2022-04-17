#include <iostream>

void jednadzba_pravca(float x1,float y1,float x2,float y2){
    float k = (y2 - y1)/(x2 - x1);
    float l = y1 - k*x1;
    std::cout << "y = " << k << "x + " << l << std::endl;
}

int main(){
    jednadzba_pravca(3,2,4,7);
    return 0;
}