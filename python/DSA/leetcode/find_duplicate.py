x = [1,2,3,3]
counter = {}
for i in x:
  if i in counter:
    counter[i] += 1
  else:
    counter[i] = 1

for y,x in counter.items():
    if x >= 2:
      print (y,'True')
    else:
      print(y,'False')