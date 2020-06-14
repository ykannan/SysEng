# Print only the words that start with s in this sentence
st = 'Print only the words that start with s in this sentence'
lst = st.split()
for i in lst:
  if i[0].lower()=='s':
    print (i)

#use range() to list all the even numbers from 0 to 10
x = range(11)
tmp = []
for i in x:
  tmp.append(i)
print((tmp)[:11:2])

#Create a list of numbers between 1 to 50 that are divisible by 3
y = range(51)
tmp=[]
for i in y:
  tmp.append(i)
print((tmp)[:51:3])

#or

for i in y:
  if i%7 == 0:
    print(i)

#go through the string and if the lenght of the word is even print "Even"
st = 'Print only the words that start with s in this sentence'
lst = st.split()
for i in lst:
  l = len(i)
  if l%2 == 0:
    print (i,l,"Even")

# FizzBuzz - multiples of 3 print "Fizz", multiples of 5 print "Buzz" multiples of 3 and 5 print FizzBuzz
x = range(101)
for i in x:
  if i%3==0 and i%5==0:
    print(i, "FizzBuzz")
  elif i%3 == 0:
    print(i, "Fizz")
  elif i%5 == 0:
    print(i, "Buzz")
  else:
    print(i, "integer")

#list comprehension - create a list of the first letters in this string
st = 'create a list of the first letters in this string'
tmp = []
ls = st.split()
for i in ls:
  tmp.append(i[0])
print(tmp)
