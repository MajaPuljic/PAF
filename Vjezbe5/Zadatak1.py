import harmonic_oscillator as HO

HO1 = HO.HarmonicOscilator()
HO1.set_initial_conditions(0.1,8,0.01,0,1)
HO1.oscillate(3)
HO1.plot()