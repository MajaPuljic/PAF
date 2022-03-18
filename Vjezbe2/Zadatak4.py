import KosiHitac as KH

KH.xy_putanja(5,45,3)
maxh = KH.max_h(5,45,3)
maxv = KH.max_v(5,45,3)
D = KH.domet(5,45,3)
KH.meta(5,5,3,5,45,3)

print("Maksimalna visina je: {} m.".format(round(maxh),3))
print("Najveća postignuta brzina je: {} m/s.".format(round(maxv),3))
print("Domet hitca je: {} m.".format(round(D),3))