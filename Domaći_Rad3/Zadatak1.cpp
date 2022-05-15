#include <Harmonic_Oscillator.h>
#include <math.h>

using namespace std;

int main(){
    HarmonicOscilator HO1(1,0,8,0.1);
    HO1.oscillate(3,0.01);
}