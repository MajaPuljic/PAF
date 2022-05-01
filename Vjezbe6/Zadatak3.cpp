#include <iostream>
using namespace std;

void ispis( int lista[]){
    int a = sizeof(lista); 
    for (int i = 0;i <a; i++){
        std::cout << lista[i] << " ";}

    }
void okretanje_redosljeda(int lista[]){
    int a = sizeof(lista); 
    for (int i = a;i >=0; i--){
        std::cout << lista[i] << " ";}

}

void zamjena_dva_clana(int lista[]){
    int a = sizeof(lista);
    int temp;
    temp = lista[0];
    lista[0] = lista[a -1];
    lista[a - 1] = temp;

}

void sortiranje(int lista[]){
    int a = sizeof(lista);
    for(int i = 0; i<= a; i++){
        for(int j=0; j<= a; j++){
            if(lista[i] < lista[j]){
                int temp = lista [i];
                lista[i] = lista[j];
                lista[j] = temp;
            }
        }
    }
    for(int i = 0; i<= a; i++){
        cout << lista[i] <<" ";
    }

}

int main(){
    int lista[4] = {2,4,3,7};
    ispis(lista);
    okretanje_redosljeda(lista);
    zamjena_dva_clana(lista);
    sortiranje(lista);
    

}



    