def non_repeating(strg):
    counter = {}
    for i in strg:
        if i in counter:
            counter[i] += 1
            print(counter)
        else: 
            counter[i] = 1
    for i in counter:
        if counter[i] == 1:
            print(i)

non_repeating('oaabrbccdecdf')




nums1 = [1,2,2,1], 
nums2 = [2,2]

# nums = [1,1,2]
# counter = {}
# for i in nums:
#   if i in counter:
#     counter[i] += 1
#   else:
#     counter[i] = 1

# for x,y in counter.items():
#   print(x,y)