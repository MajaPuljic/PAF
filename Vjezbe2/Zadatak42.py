import KosiHitac2 as kh

v0 = 5
kut = 0.7
y0 = 4
p = 4
q = 7
r = 1


hmaks = kh.maks_visina(v0, kut, y0)
vmaks = kh.maks_brzina(v0, kut, y0)
d = kh.domet(v0, kut, y0)

print("Maksimalna visina je: ", hmaks, "m.")
print("Najveća postignuta brzina je", vmaks, "m/s.")
print("Domet hitca je: ", d, "m.")