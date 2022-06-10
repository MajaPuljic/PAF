#include <iostream>

void interval(int lista[], int i1, int i2, int size){
    if(i1 >= 0 && i2 < size){
        for(int i = i1; i < i2 + 1; i++){
            std::cout << lista[i] <<std::endl;
        }
    }
    else{
        std::cout << "Unijeli ste raspon veći od duljine liste";
    }
    
    
}
//kako returnat listu??
void obrat(int lista[], int size){
    int obrnuta[size];
    for(int i = 0; i < size; i++){
        obrnuta[i] = lista[size - 1 - i];
        //std::cout << i << std::endl;
        //std::cout << obrnuta[i];
    }
    for(int j = 0; j < size; j++){
        lista[j] = obrnuta[j];
    }
}

void zamjena(int lista[], int i1, int i2){
    int temp;
    temp = lista[i2];
    lista[i2] = lista[i1];
    lista[i1] = temp;
}

void sortiranje(int lista[], int size){
    int temp;
    for(int i = 0; i < size; i++){
        for(int j = i+1; j < size; j++){
            if (lista[j] < lista[i]){
                temp = lista[i];
                lista[i] = lista[j];
                lista[j] = temp;

            }
        }
    }
    for(int i = 0; i < size; i++){
        std::cout << lista[i] << " ";
    }
    
}

int main(){

     int lista[5] = {1,2,3,4,5};

    int nesortirana[5] = {5, 7, 2, 33, 1};
    interval(lista, 1, 4, 5);
    obrat(lista, 5);
    zamjena(lista, 2, 3);
    sortiranje(nesortirana, 5);
    return 0;
}

    