#Luo esimerkkien avulla 20-alkioinen taulukko, joka sisältää satunnaisia kokonaislukuja.
# Saat itse päättää minkä kokoisia. Järjestä luvut suuruusjärjestykseen ja lopuksi muunna
# taulukkoo kaksiulotteiseksi taulukoksi, jossa on viisi alkiota per rivi.

import numpy as np

array = np.random.randint(1, 101, 20)
print(f"20-alkioinen taulukko:")
print(array)
array.sort()
new_array = array.reshape(4, 5)
print(f"Kaksiulotteinen taulukko järjestettynä:")
print(new_array)
print(80*"-")
#Sinulla on vektorit a) u = 2i + 3j, v =4i - 7j
# b) uu= i + j + k, vv 3i -3j + 2k.
# Määrittele nämä numpy taulukon avulla.
# Laske kunkin vektorin normi.

#a.
u = np.array([2,3])
print(f"Vektorin u = 2i + 3j normi on {np.linalg.norm(u):.2f}")
v = np.array([4, -7])
print(f"Vektorin v = 4i - 7j normi on {np.linalg.norm(v):.2f}")

#b.
uu = np.array([1, 1, 1])
print(f"Vektorin uu= i + j + k normi on {np.linalg.norm(uu):.2f}")
vv = np.array([3, -3, 2])
print(f"Vektorin vv = 3i -3j + 2k normi on {np.linalg.norm(vv):.2f}")
