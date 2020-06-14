x = [2,2,1]
counter = {}

for i in x:
  if i in counter:
    counter[i] += 1
  else:
    counter[i] = 1

for y,z in counter.items():
  if z == 1:
    print (y,z)