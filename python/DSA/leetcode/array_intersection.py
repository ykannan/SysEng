# extracting common objects
nums1 = [4,9,5]
nums2 = [9,4,9,8,4]

# def intersection(nums1, nums2):
#   nums3 = [x for x in nums1 if x in nums2]
#   return nums3
# print(intersection(nums1, nums2))

temp = []
for x in nums1:
  if x in nums2:
    temp.append(x)
print(temp)