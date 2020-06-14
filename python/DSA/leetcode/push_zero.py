# mutating or changing list using idex values
lst = [0,1,0,3,12]

l = len(lst)
r = range(l)

def push(lst,r):
  count = 0 
  for i in r:
    if lst[i] != 0:
      lst[count] = lst[i]
      count += 1

  while count < l:
    lst[count] = 0
    count += 1
  print(lst)

push(lst,r)
