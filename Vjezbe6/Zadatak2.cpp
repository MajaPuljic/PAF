#include <iostream>
#include <math.h>

void odnos_tocke_i_kruznice(float xr,float yr,float r,float x,float y){
    float d = sqrt((x-xr)*(x-xr)+(y-yr)*(y-yr));
    if (d <= r){
        std::cout<< "Tocka se nalazi unutar kruznice"<<std::endl;
    }
    else{
        std::cout<< "Tocka se nalazi van kruznice"<<std::endl;
    }
}

int main(){
    odnos_tocke_i_kruznice(5,6,3,10,11);
    return 0;
}