#capitalize the 1st and 4th letter of the name
x = 'macdonald'
first = x[0]
fourth = x[3]
rest = x[1:3]
rest2 = x[4:]
print(first.upper()+rest+fourth.upper()+rest2)

#given a sentence return a sentence with words reversed
x = 'I am home'
ls1 = x.split()
rev1 = ls1[::-1]
print(' '.join(rev1))

#given integer n return true if n is within 10 of either 100 or 200
n = 90

if abs(100-n) <= 10 or abs(200-0) <= 10:
  print("True")
else:
  print("False")

#Given a list of ints, return true if the array contains a 3 next to 3 somewhere
x = [1,3,2,3]
l = len(x)

for i in range(l-1):
  if x[i] == 3 and x[i+1] ==3:
    print(x[i],"True")
  else:
    print("False")

#Given a string, return a s string where for every character in original there are 3 characters
# Input: 'Hello' Output: 'HHHeeelllooo'
x = 'Hello'
tmp=[]
for i in x:
  tmp.append(i*3)
print(''.join(tmp))

# BlackJack - Given 3 integers between 1 and 11 if their is less than 21 return sum. If their sum is greater than 21 and if there is a 11 present, subtract 11 from their total value. Even if the sum is greater than 21 after subtracting 11 return BUST
x = [32,6,11]
s = x[0] + x[1] + x[2] 
if s <= 21:
  print(s)
elif s <= 31 and 11 in x:
  print(s-10)
else:
  print("BUST")

#summer of 69. Return sum of numbers in an array except ignore numbers starting with a 6 abd extending to the next 9.
lst = [4,5,6,7,8,9]
total = 0 
boo = True
for i in lst:
  while boo:
    if i != 6:
      total += i
      break
    else:
      boo = False
  while not boo:
    if i != 9:
      break
    else:
      boo = True
      break

print(total)

#write a function that takes in a list of integers and returns True if it contains 007 in order

lst = [1,2,3,0,0,7,0,5]
sub_lst = [0,0,7]

str1 =''
str2 =''
for i in lst:
  str1 += str(i)
for i in sub_lst:
  str2 += str(i)
print(str1,str2)
l1 = len(str1)
l2 = len(str2)
tmp = 0
for i in range(l1 - l2):
  if str1[i:l2 + i] == str2:
    tmp += 1
    print("True")
print(tmp)
