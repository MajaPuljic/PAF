#include <iostream>
#include <vector>
#include<fstream>
#include <string>

using namespace std;

class HarmonicOscilator{

    private:
        float x0;
        float x;
        float v0;
        float v;
        float t;
        float m;
        float k;
        float a;

        void evolve(float dt){
            a = -(k/m)*x;
            v = v + a*dt;
            x = x + v*dt;
            t = t + dt;
            x_lista.push_back(x);
            v_lista.push_back(v);
            a_lista.push_back(t);
            t_lista.push_back(t);

        };

    public: 
        vector<float> x_lista;
        vector<float> v_lista;
        vector<float> a_lista;
        vector<float> t_lista;


        HarmonicOscilator(float x0_, float v0_, float k_, float m_ ){

            x0 = x0_;
            v0 = v0_;
            k = k_;
            m = m_;
            x = x0;
            v = v0;
            a = -(k/m)*x;
            t = 0;
            x_lista.push_back(x);
            v_lista.push_back(v);
            a_lista.push_back(t);
            t_lista.push_back(t);
            }

        void oscillate(float t_uk, float dt){
            while(t< t_uk){
                move(dt);
            };

        };

};
