#combine all the repeated characters using set #Udemy
# x = 'Mississippi'
# y = set(x)
# print(y)




s = "loveleetcode"
counter = {}
for i in s:
  if i in counter:
    counter[i] += 1
  else:
    counter[i] = 1

# find index position in the string using .index
for x,y in counter.items():
  if y == 1:
    z = s.index(x)
    print(z)