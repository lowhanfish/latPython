import numpy as np

# Membuat vector
a = np.array([1,2,3])
b = [4,5,6]


a = a + 1
b = b + [1]

# membuat vector dengan range
c = np.arange(0,10,2)

# membuat linspace. maksud kode (kita mulai dari mana, berahir di mana, kita mau bagi rata berapa bagian yang ditampilkan)
d = np.linspace(1,10,4)

# Membuat array multidimensi
e = np.array(
    [
        (1,2,3),
        (4,5,6)
    ]
)

# matrix zero 1D
f = np.zeros(5)

# matrix zero 2D 5x2 
g = np.zeros((5,2))

# matrix dengan nilai 1, sama saja seperti zero tapi paketnya beda
h= np.ones(5)


# matrix diagonal / indentitas ada dua cara
i1 = np.identity(5)
i2 = np.eye(5)

# Print
print(i1)

