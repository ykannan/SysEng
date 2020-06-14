#Remove Duplicates from Sorted Array
nums = [0,0,1,1,1,2,2,3,3,4]

counter = {}
for i in nums:
  if i in counter:
    counter[i] +=1
  else:
    counter[i] = 1

for x,y in counter.items():
    print(x,y)
print(len(counter))
