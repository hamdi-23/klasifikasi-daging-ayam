import numpy as np 
import math
image = np.array([[3,4,5],[5,6,7],[2,3,4]])

jumlah = image.sum()
ukuran = image.size

print(jumlah)
print(ukuran)

hasil = jumlah/ukuran

print(hasil)

stdef=math.sqrt(((image-hasil)**2).sum()/ukuran)
print(stdef)

sqew = (((image-hasil)**3).sum()/ukuran)
g = sqew**(1/3)
print(g)