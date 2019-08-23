mystring = 'hello'
mylist = []

# Method -1 Inputting string into list
for x in mystring:
     mylist.append(x)
     print(x)
print(mylist)
    
# Method-2 list comprehension, flattened out for loop
mylist_2 = [x for x in 'word']
print(mylist_2)

mylist_3 = [y**2 for y in range(0,10)]               # squaring values in the list
print(mylist_3)

mylist_4 = [y+3 for y in range(0,30) if y%2==0]      # adding + modding
print(mylist_4)

celcius = [0,45,94.1]
Fahrenheit = [x*(9/5)+32 for x in celcius]
print (Fahrenheit)