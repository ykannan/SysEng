# for loop

x = [1,2,3,'happy']

for i in x:
    print ('the number is {numb}'.format(numb = i))

# checking for even numbers 
y = [1,2,3,4,5,6,7,8,9,10,11,12,13]
for a in y:
    if a % 2 == 0:
        print ('{odd} even numbers'.format(odd = a))
    else:
        print ('{odd} odd numbers'.format(odd = a))

# checking sum
list_sum = 0 
for b in  y:
    list_sum = list_sum + b
    print (list_sum)     # prints running values and sum
print (list_sum)         # prints final sum when outside the condition 

 # iterating values in tuple
tuple = (1,2,3,'one',5)
for z in tuple:
    print (z)

# iterating tuples vaues in list 
list_tuple = [(1,2),(3,4),(7,8,9)]  
for o in list_tuple:
    print(o)

# iterating tuple values in list 
list_tuple = [(1,2),(3,4),(7,9)]  
for a,b in list_tuple:
    print(a)
    print(b)

# iterating dictionary 
d = {
    'a' : 1,
    'b' : 2,
    'c' : 3,
}
for dict in d.items():
     print (dict)

for dict in d.keys():
     print (dict)

for dict in d.values():
     print (dict)