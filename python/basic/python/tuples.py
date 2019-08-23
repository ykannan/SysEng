x = ('one',2,3) # tuple = (), immutable --> cannot assign values, can be used for data intergrity 
y = [1,2,3]
y[0] = 20       # mutating value in a list 
print (y)

x[0] = 2        # cannot mutate values in a tuple (immutable)
print (x)