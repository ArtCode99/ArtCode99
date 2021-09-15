import numpy as np

#NUmpy poate crea seturi de date de pana la 3 dimensiuni (array,matrix sau 3d) si asta  se modifica cu shape.
#NUmpy e mult mai rapid decat listele, deoarece listele contin mult mai multa informatie, gen reference count, object type, value, in timp ce numpy pastreaza doar binaru
# Differentele mai sunt si ca in numpy mai poti sa faci si altele decat insertion,deletes, searches ca in liste.

#Ca sa creezi un array:
z=np.array([1,2,3])
print(z)

b=np.array([[9,5,6,8],[6,4,1,4]])     #bidimensional
# print(b.ndim)
#Mai putem sa aflam dimensiunile+forma si cu shape:
# print(b.shape)

#Putem sa inmultim liste aici:
# mult=z*np.array([2,3,1])
# print(mult)

#Accesarea unui anumit element : [row_index,col_index]
# print(b[1,3])
#Accesarea unui rand:
# print(b[0, :])


## Matricea identitate: (exista multe functii pt creare de anumite array-uri)
# print(np.identity(3))
# print(np.ones((5,5)))

#ATENTIE CAND COPIEZI ARRAY-URI! , ca daca modifici ceva in ala copiat se modifica si ala initial, e un fel de pointer
#ca sa te feresti de asta poti sa folosesti .copy()

c=b.copy()
print(c)