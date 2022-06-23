import VertikalniHitac as VH

objekt_1 = VH.Projektil(17,9)
objekt_2 = VH.Projektil(5,15)

objekt_1.promjena_h0(13)
objekt_2.promjena_v0(8)

print("Pocetna visina prvog objekta je sada: {} m \nPocetna brzina drugog objekta je sada: {} m/s".format(objekt_1.h,objekt_2.v))

