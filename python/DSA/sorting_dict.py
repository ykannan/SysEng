# sort dictonary 
import operator
dic  = {
  2:3,
  5:6,
  1:2,
  3:4,
  4:5,
  
}

asc = sorted(dic.items(), key=operator.itemgetter(1))
des = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
for i in asc:
  print (i) 
for i in des:
  print (i)

# combine dic
dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}
dic4 = {}

d = dic1.copy()
d.update(dic2)
print (d)
 

for i in (dic1,dic2,dic3):
  dic4.update(i)
  
print (dic4)

# find if the value is present in a dic
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

def find(i):
  if i in d:
    print ("{r} is presenti".format( r = i))
  else:
    print("i is not present")
  
find(1)

# iterate over the keys and values using loops
d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

for x,y in d.items():
  print(x,y)

# 6. Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x). Go to the editor
# Sample Dictionary ( n = 5) : 
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

dic = {}
n = 5
for i in range(n,n+1):
  dic[i] = i*i
print(dic)

#7Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are square of keys.
d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)

# multiply values 
dic1={1:10, 2:20, 3:30, 4:40}

total = 1
for i in dic1.values():
  total = total*i
print(total)
 
print(sum(dic1.values()))

#map lists
keys = ['red', 'green', 'blue']
values = ['#FF0000','#008000', '#0000FF']

x = dict(zip(keys,values))
print(x)

for i in x:
  print(i)

# remove duplicates
student_data = {'id1': 
   {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id2': 
  {'name': ['David'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id3': 
    {'name': ['Sara'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
 'id4': 
   {'name': ['Surya'], 
    'class': ['V'], 
    'subject_integration': ['english, math, science']
   },
}


d = {}

for x,y in student_data.items():
  if y not in d.values():
    d[x] = y
print(d)
    
# check for empty dict
d = {}

if bool(d) == False:
  print("null dict")

  # adding dict 
from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)