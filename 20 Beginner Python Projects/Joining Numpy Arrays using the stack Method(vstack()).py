#  Join Numpy Arrays - Stack Method(vstack())

import numpy as np

c = np.array([4,6,9])
c1 = np.array([12,17,21])

# Stack two arrays vertically
c2 = np.vstack((c1,c))
print(c2)

c2 = np.vstack((c,c1))
print(c2)

# Iterate through the stacked array
for f in c2:
    print(f)
# Iterate through the first array in the stack
for f in c:
    print(f+1)

# Iterate through the second array in the stack
for f in c1:
    # print(f+2)
    print(f+1+1)

# Using while loop to iterate through the stacked array
g = 0
while g < len(c2):
    print(c2[g])
    print(c2[g]+1)
    g+=1

# Using while loop to iterate through the first array in the stack
g = 0
while  g < len(c2):
    print(c1[g]+1)
    print(c[g]+2)
    g+=1
