# .format() method
print ("this is a {} string and {} likes it {}".format("nasty", "Yogesh", "a lot")) # using tuples
print ("this is a {1} string and {2} likes it {0}".format("nasty", "Yogesh", "a lot")) # using tuple indexes
print ('this is a {n} string and {Y} likes it {l}'.format(n= 'nasty', Y= 'Yogesh', l= 'a lot')) # using keywords

result = 100/77
print ('This is the result {r:1.5f}'.format(r = result)) #using float formatting 1 --> Width .5f --> precision


# Fstring() method
name = 'Yogi' 
age = 3
print(f'His name is {name}')
print (f'His name is {name}. His age is {age}')

# reversing strings [<start>>:<stop>:<step>]
x = '123456789'[0:10:-1]        # reversing a string 
y = '123456789'[0:-19:-1]       # reversing + slicing a string 
z = '123456789'[0:16:3]         # slicing  
print (x)
print (y)
print (z)