import numpy as np

#Tehtävä 3 matriisilaskentaa
A = np.array([[-1, 2], [3, -5]])
B = np.array([[2, 0], [-1, 4]])
print(f"A ={A}")
print(f"B ={B}")
print(80*"-")
# C= 2A+3B
C = (2*A + 3*B)
print("2A+3B=")
print(C)
print(80*"-")
# D = A-B
D = (A-B)
print("A-B =")
print(D)
print(80*"-")
print(80*"-")

#Yhtälöryhmät numpyllä
#1a. 5x+3y = 9
#    2x+y = 4

A = np.array([[5, 3], [2, 1]])
B = np.array([9, 4])
X = (np.linalg.inv(A).dot(B))
print(f"Tehtävä 1 a: x={X[0]:.0f} ja y={X[1]:.0f}")
print(80*"-")

#1b. 2x+y+z=6
#   x+3y+z=2
#   2x+y+2z=9

A = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
B = np.array([6, 2, 9])
X = (np.linalg.inv(A).dot(B))
print(f"Tehtävä 1 b: x={X[0]:.0f} ja y={X[1]:.0f} ja z={X[2]:.0f}")
print(80*"-")

#1c. x+y+3z=-1
#   3x+y+z=5
#   2x+y+2z=2

#Seuraavat luo errorin
# A = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
# B = np.array([-1, 5, 2])
#X = (np.linalg.inv(A).dot(B))
print("1 c: Determinantti 0, ei voi luoda känteismatriisia.")
