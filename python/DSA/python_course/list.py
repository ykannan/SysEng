# converting a string intro a list using .split()
x = 'Yogesh Kannan Iyyengar'
y = x.split()
for i in y :
  print(i)

#list concat
a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

#appending item at the end of the list using .append()
q = [1,2,3] 
d = q.append(6)
print(q)

#removing item at the end of the list using .append()
e = q.pop(0)
print (q)

#sorting and reversing .sort()
lst = [0,5,78,9,6,3,2,1,4]
lst.sort()
print(lst)

lst_1 = [0,5,78,9,6,3,2,1,4]
lst_1.reverse()
print(lst_1)