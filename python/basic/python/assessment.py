#1 Split
st = 'print only the words that start with s in the sentence'
split = st.split() #gives out a list
print (split)

for i in split:
    if i.startswith('s'):
        print (i)



# 2 Range 
even1 = list(range(0,16))
even = [x for x in range(0,11)]
print(even)
print(even1)

# 3 list comprehension
div = [y for y in range (1,51) if y%3==0]
print (div)

# 4 print words with even number length
mystring = 'Print every word in this sentence that has an even number of letters'
o = mystring.split()

for i in o:
    if len(i)%2==0:
        print(i +' is even')

# 5 Job_Password108!
for value in range(1,100):
    if value%3==0 and value%5==0:
        print('FizzBuzz')
    elif value%5==0:
        print('Fizz')
    elif value%3==0:
        print('Buzz')
    else:
        print (value)

#6 

st2 = 'Create a list of the first letters of every word in the string'
p = [w[0] for w in st2.split()]
print(p)

# method 2
g = st2.split()
print(g)
for i in g:
    print (i[0])
