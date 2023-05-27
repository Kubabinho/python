import numpy as np

#generate 5x5 array with random integers between 0 and 4
tab1 = np.random.randint(0, 5, size=(5, 5))

print(tab1)

#find minimum value in the array
min1 = np.min(tab1)

#find maximum value in the array
max2 = np.max(tab1)

print(min1)
print(max2)

#find maximum value along the columns (axis=0)
print(np.max(tab1, axis=0))

#find maximum value along the rows (axis=1)
print(np.max(tab1, axis=1))

#calculate sum of each row
print(np.sum(tab1, axis=1))
