import numpy as np

#create list containing powers of 2 in descending order
l1 = [128, 64, 32, 16, 8, 4, 2, 1]
for i in range(7, -1, -1):
    l1.append(2**i)

#create list containing powers of 2 in descending order using list comprehension
l2 = [2**i for i in range(7, -1, -1)]

print(l1)
print(l2)

#convert list into numPy array
tab_1 = np.array(l2)
print(tab_1)

#generate a random binary array of length 8
num_bin = np.random.randint(0, 2, 8)
print(num_bin)

#perform element-wise multiplication of `tab_1` and `num_bin` to get `num_dec`
num_dec = tab_1 * num_bin
print(num_dec)

#calculate sum of all elements
print(num_dec.sum())
