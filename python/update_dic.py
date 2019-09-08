#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

dic = {
  0:10,
  1:20
}

dic[2]=30
print(dic)


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)


#match dict
a = {
   'key1': 1, 
   'key2': 3, 
   'key3': 2}
 
b = {
   'key1': 1, 
   'key2': 2}

for x,y in a.items() & set(b.items()):
  print(x,y)
  
  
  for x,y in a.items():
    for k,v in b.items():
      if x == k and y == v:
        print(x,v)



