#Range
for x in range(0,10,2):
    print (x)

# Generating a list 
x = list(range(0,10))
print (x)

# ENUMERATE function to print index values 
z = 'This is a long string and we need to know the index value of each'
for i,o in enumerate(z):
    print (i,o)
    print('\n')

# ZIP function to print index values 
z = 'This is a long string and we need to know the index value of each'
w = [1,2,3,4,5,6,7,5,9,10,11,12,13]
c = zip(z,w)
for i in c:
    print (i)

# Printing min & max numbers in a list or string 
w = [1,2,3,4,5,6,7,5,9,10,11,12,13]
m = min(w)
r = max(w)
print (m)
print (r)

# Shuffling and Random Integer
from random import shuffle
from random import randint
w = [1,2,3,4,5,6,7,5,9,10,11,12,13]
f = randint(1,100)
#u = shuffle (w)         # need to figure out
print (f)

# Input function to promt input
r = input ('Enter a number here: ')
print (r)





# Note for list [::], for range(,,) refer string_format.py
# zip allocates indexes based on the number of indexes in list, others are ignored