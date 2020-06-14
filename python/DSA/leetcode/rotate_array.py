#slicing
lst = [1, 2, 3, 4, 5]
n = len(lst)
r = range(n)

for x in r:
  last = lst[n-1]
  for y in range(n-1,-1),-1:
    lst[y] = lst[y-1]