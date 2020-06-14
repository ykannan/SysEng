lst = [2, 7, 11, 15, 1]

# l = len(lst)
# r = range(l)
# def two_sum(lst,r):
#   count = {}
#   for i in r:
#     for j in lst:
#       if lst[i] + j == 9:
#         print (lst[i],j)
#         count[9] = (lst[i],j)
  
#   for i,j in count.items():
#     print(i,j)
# two_sum(lst,r)

#simple method
l = len(lst)
r = range(l-1)  # -1 give [0,1,2] i+1 gives 4.Else it goes out of range

for i in r:
  if lst[i] + lst[i+1] == 9:
    print (i,i+1)

# lst.sort(reverse=True)
lst.reverse()
print(lst)