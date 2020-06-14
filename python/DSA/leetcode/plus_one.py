x = [4,3,2,1]

# n = len(x)
# x[n-1] = x[n-1]+1
print(x)
# lsit > string > integers > string > list 
#convert list to string
string = ''
for i in x:
    string += str(i)
print(string)
#convert string to integers
integer = int(string)
integer += 1
print (integer)

#convert integers to string
integer = str(integer)

#convert string to list
ans = []
for i in integer:
    ans.append(int(i))
print(ans)
