# sample = 'abefhefcdefhab'
#
# match_string = ['e', 'f', 'h']
#
# word_length_map = []
# word_length = 0
# match_pattern = ''
#
# for i, character in enumerate(sample):
#     if character in match_string:
#         word_length += 1
#         match_pattern += character
#
#     else:
#         if word_length >=3:
#             word_length_map.append(match_pattern)
#             word_length = 0
#             match_pattern = ''
#
# word_length_map.append(match_pattern)

# word_length_map[match_pattern] = word_length
#
# print(word_length_map)
# for k, v in word_length_map.items():
#     print(k, v)
#

#Optimized
# word_length_map.sort()
# print(word_length_map[-1])

# PROBLEM
# tableData = [['apples', 'oranges', 'cherries', 'banana', 'dragonfruit'],
#              ['Alice', 'Bob', 'Carol', 'David', 'Steve'],
#              ['dogs', 'cats', 'moose', 'goose', 'lioness'],
#              ['India', 'Europe', 'Iceland', 'Canada', 'Japan']]
#
# """
#      apples Alice    dogs
#     oranges   Bob    cats
#    cherries Carol   moose
#      banana David   goose
# dragonfruit Steve lioness
# """
#
# results = []
# final = []
# list_length = 0
# elements_length = 0
# long_str = {}
#
#
# def printTable(tableData, list_length):
#
#     # Get the max elements which exists inside list of list
#     for elements in tableData:
#         if list_length != len(elements):
#             list_length = len(elements)
#
#     # To create keys to store the maximum length of string in the list of ist
#     for i, names in enumerate(tableData):
#         col = 'col'
#         col = col + str(i+1)
#         max_length = 0
#         for name in names:
#             if len(name) > max_length:
#                 max_length = len(name)
#                 long_str[col] = max_length
#             else:
#                 pass
#
#     # To gather the elements across multiple lists based on their index value
#     for iteration in range(list_length):
#         initial_list = []
#         for element in tableData:
#             initial_list.append(element[iteration])
#         results.insert(iteration, initial_list)
#
#     # To right adjust all the elements in the list of list
#     for i, result in enumerate(results):
#         indent_list = []
#         for index in range(len(result)):
#             col_no = 'col' + str(index+1)
#             indent_list.append(result[index].rjust(long_str[col_no]))
#         final.insert(i, indent_list)
#
#     # To get the string like output
#     for final_element in final:
#         print(' '.join(final_element))
#
# printTable(tableData, list_length)


# input_str = 'pwwkewbyuhawgqxyioplksd'
# s = 'pwwkewbyuhawgqxyioplksd'
# # input_str = 'pwwkewbyuhaw'
# input_str = ' '
#
# used_chars = set()
# count = 0
# max_count = 0
# start_index = 0
# i = 0
# while i < len(s):
#     print(s[i],i)
#     if s[i] not in used_chars:
#         used_chars.add(s[i])
#         count += 1
#         i += 1
#     else:
#         print(s[start_index], start_index)
#         count = count - 1
#         used_chars.remove(s[start_index])
#         start_index += 1
#     print(used_chars)
#     max_count = max(count, max_count)
# print(max_count)

# char_list = []
# substring = ''
# long_list = set()
#
# for char in input_str:
#     char_list.append(char)
#
# for i in range(0, len(input_str)):
#
#     if i == 0:
#         substring += char_list[i]
#
#     elif char_list[i] is not char_list[i-1]:
#         if char_list[i] not in substring:
#             substring += char_list[i]
#             long_list.add(substring)
#         else:
#             long_list.add(substring)
#             substring = ''
#             substring += char_list[i]
#
#     else:
#         long_list.add(substring)
#         substring = ''
#         substring += char_list[i]
#
# print(long_list)
# if len(long_list) > 0:
#     print(len(sorted(long_list, key=len)[-1]))
# else:
#     print("")

# kewbyuha
# wgqxyioplksd

# PROBLEM
# max_int = [-2, 1, -3, 4, -1, 2, 1, -5]
#
# list_sum = []
#
#
# def max_integer(max_int):
#     max_value = 0
#     sum = max_int[0]
#
#     for n in range(1, len(max_int)):
#         if (max_int[n] + sum) >= max_int[n]:
#             sum += max_int[n]
#             list_sum.append(sum)
#         else:
#             sum = max_int[n]
#
#     return max(list_sum)
    # for value in list_sum:
    #     if value > max_value:
    #         max_value = value

    # return max_value

# print(max_integer(max_int))

# sent_input = ""
#
#
# def length_of_string(sent_input):
#
#     if sent_input:
#         return 0 if not sent_input.split(" ")[-1] else len(sent_input.split(" ")[-1])
#
#     else:
#         return 0
#
# print(length_of_string(sent_input))

# PROBLEM
# nums = [1]
# nums = [5,7,7,8,8,10]
# target = 8
#
#
# def search_array(nums, target):
#     target_index = []
#     if target in nums:
#         for right_i, n in enumerate(nums):
#             if target == n:
#                 target_index.append(right_i)
#                 break
#
#         for left_i in range(len(nums)-1, -1, -1):
#             if target == nums[left_i]:
#                 target_index.append(left_i)
#                 break
#         return target_index
#     else:
#         return [-1, -1]
#
# print(search_array(nums, target))


# x = 123
#
# reverse_number = ''
# if x in range((-2**31), (2**31)):
#    for number in :
#         print(number)
# else:
#     print("0")

# PROBLEM
# s = 'RLRRLLRLRLLLRR'
# substring = ''
# substrings_list = []
# r_count = 0
# l_count = 0
#
# for char in s:
#     if 'R' is char:
#         substring += char
#         r_count +=1
#
#     else:
#         substring += char
#         l_count +=1
#
#     if r_count == l_count:
#         substrings_list.append(substring)
#         substring = ''
#         r_count = 0
#         l_count = 0


# print(len(substrings_list))
# print(substrings_list)

#
# from itertools import accumulate
#
# print (list(accumulate(1 if c == "R" else -1 for c in s)))
# print(list(accumulate(1 if c == "R" else -1 for c in s)).count(0))

# char = "IDID"
#
# i_index = 0
# d_index = len(char)
# letter_list = []
# for i, s in enumerate(char):
#     if s is 'D':
#         letter_list.append(d_index)
#         d_index -= 1
#         if len(char) == i+1:
#             letter_list.append(d_index)
#     else:
#         letter_list.append(i_index)
#         i_index += 1
#         if len(char) == i+1:
#             letter_list.append(i_index)
#
# print(letter_list)

# PROBLEM
# nums = [2,2,1,1,1,2,2]
# map_num = {}
# uniq_num = set(nums)
# for num in uniq_num:
#     map_num[num] = nums.count(num)
#
# max_value = 0
# for k, v in map_num.items():
#     if v >= max_value:
#         max_value = v
#         max_key = k
#
# print(max_key)

# from collections import defaultdict
#
# chars = ["a","a","b","b","a","a","a"]
#
# char_count = defaultdict(int)
#
# for c in chars:
#     char_count[c] += 1
# 
# print(list(char_count.keys()) + list(char_count.values()))

# dict_char = {}
# count = 0
# final_list = []
# for char in chars:
#     if char not in dict_char.keys():
#         dict_char[char] = 1
#
#     else:
#         dict_char[char] = dict_char[char] + 1
#
# for char, char_value in dict_char.items():
#     if char_value == 1:
#         final_list.append(str(char_value))
#         continue
#
#     else:
#         final_list.append(char)
#
#     final_list.append(str(char_value))
#
# print(final_list)
# print(len(final_list))


# chars = ["a","a","b","b","c","c","c"]

# new_list = ''
# dict_char = {}
# for i , c in enumerate(chars, start=0):
#
#     if i == 0:
#         dict_char[c] = 1
#         new_list += c
#         continue
#
#     if c in dict_char.keys():
#         dict_char[c] = dict_char[c] + 1
#
#     else:
#         if dict_char[chars[i-1]] > 1:
#             new_list += chars[i-1]
#             new_list += str(dict_char[chars[i-1]])
#             dict_char = {}
#             dict_char[c] = 1
#         else:
#             new_list += chars[i - 1]
#             dict_char = {}
#             dict_char[c] = 1
#
#
#     if i == (len(chars) - 1) and dict_char[chars[i-1]] > 1:
#         new_list += chars[i - 1]
#         new_list += str(dict_char[chars[i - 1]])
#
#
# chars = [c for c in new_list]
# print(chars)

# chars = ["a","a","b","b","c","c","c"]
# rptr, wptr = 0, 0
# while rptr < len(chars):
#     ch, f = chars[rptr], 0
#     while rptr < len(chars) and chars[rptr] == ch:
#         rptr, f = rptr + 1, f + 1
#     chars[wptr], wptr = ch, wptr + 1
#     print("Charrr {}".format(chars))
#     if f > 1:
#         for c in str(f):
#             chars[wptr], wptr = c, wptr + 1
#             print(chars[wptr])
#             print("Charrr ---{}".format(chars))
# print(chars)
# print(wptr)


# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

# Shouldnt use another array

# input_list = ["H","a","n","n","a","h"]
# swap_var = ''
# min_element = 0
# for i in range(len(input_list)-1, -1, -1):
#     swap_var = input_list.pop()
#     input_list.insert(min_element, swap_var)
#     min_element += 1

# Given a string, you need to reverse the order of characters in each word
# within a sentence while still preserving whitespace and initial word order.
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

# s = "Let's take LeetCode contest"
# word_list = s.split(" ")
# for i, word in enumerate(word_list):
#     word_list[i] = word[::-1]
#
# return ' '.join(word_list)

# Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

# from collections import OrderedDict
# s = "leetcode"
# return 0.
#
# s = ""
# s = "loveleetcode"
# s = "lovelevettccodde"
# return 2.

# class Solution:
#     def firstUniqChar(self, s):
#         dict_char = OrderedDict()
#         # min_value = 0
#         for char in s:
#             if char not in dict_char:
#                 dict_char[char] = 1
#             else:
#                 dict_char[char] += 1
#
#
#         for k, v in dict_char.items():
#             if v == 1:
#                 return s.index(k)
#         return -1
#
# class_ins = Solution()
# print(class_ins.firstUniqChar(s))

#
# Input: "abbaca"
# Output: "ca"

# S = "abbaca"
# i = 1

# for char in S:

# S = "aababaab"
# S = "abbaca"

# res = []
# for c in S:
#     if res and res[-1] == c:
#         res.pop()
#     else:
#         res.append(c)
# print("".join(res))
#

# import re
#
# last = None
# while last != S:
#     print(re.sub(r'(.)\1', '', S))
#     last, S = S, re.sub(r'(.)\1', '', S)
#
# print(S)


# import re
# str1 = "ABABABABAB"
# # str1 = "ABCABC"
# # str2 = "ABC"
# str2 = "ABAB"
#
# divisor_string1 = []
# for str1_i in range(1, len(str1)+1):
#     if len(str1) % str1_i == 0:
#         divisor_string1.append(str1_i)
#
#
# divisor_string2 = []
# for str2_i in range(1, len(str2)+1):
#     if len(str2) % str2_i == 0:
#         divisor_string2.append(str2_i)
#
# max_divisor = max(list(set(divisor_string1) & set(divisor_string2)))
# if max_divisor > 0:
#
#     regex_string = r'' + str1[:max_divisor]
#     if re.sub(regex_string, '', str1) == '' and re.sub(regex_string, '', str2) == '':
#         print(regex_string)
#
#     else:
#         print('')


# import re
# str1 = "ABABABABAB"
# str1 = "ABC"
# str2 = "ABCABCXX"
# str2 = "ABAB"

# if len(str1) < len(str2):
#     str1, str2 = str2, str1
#
# while str2:
#
#     a = len(str1) % len(str2)
#     n = len(str1) // len(str2)
#
#     if a == 0 and str1 != str2 * n or a > 0 and str1[:-a] != str2 * n:
#         print('')
#
#     if a == 0:
#         print(str2)
#
#     str1, str2 = str2, str1[-a:]
# print(str2)
# regex_string = r'' + str1[:2]
#
# str1_regex = re.sub(regex_string, '', str1)
# print(str1_regex)

# Remove vowels from String

# import re
#
# s = 'this is to test vowels aieou'
# s_remove = re.compile(r'[^aeiou]')
# print(''.join(s_remove.findall(s)))

# PROBLEM
# text = "thestoryofleetcodeandme"
# words = ["story","fleet","leetcode"]
#

# text = "ababa"
# words = ["aba", "ab"]

# index_word_list = {}
# for word in words:
#     for i in range(len(text) - len(word)+1):  # 0, 1, 2
#         if text[i:i+len(word)] == word:
#             if word not in index_word_list.keys():
#                 index_word_list[word] = [[i, i+(len(word)-1)]]
#             else:
#                 index_word_list[word] = index_word_list[word] + [[i, i+(len(word)-1)]]
# print(index_word_list)

# for word in words:
#     split_text = text
#     check_string = ''
#     min_post, max_post = 0, 0
#     char_pos = 0
#     for i in range(len(text)):
#         if i == 0:
#             split_text = text[max_post:]
#         elif max_post > 1:
#             split_text = text[(max_post - 1):]
#         else:
#             split_text = text[max_post:]
#
#         if len(split_text) >= len(word):
#             if word in split_text and i > char_pos:
#                 min_post = split_text.index(word) + i
#                 max_post = min_post + (len(word) - 1)
#                 check_string += text[min_post: max_post + 1]
#                 char_pos = min_post
#                 if check_string == word:
#                     index_word_list.append([min_post, max_post])
#                     check_string = ''
#
#         else:
#             check_string = ''
#
# print(sorted(index_word_list))


#PROBLEM
# num1 = "546"
# num2 = "956"
#
# num1, num2 = list(num1), list(num2)
# carry, res = 0, []
# while len(num2) > 0 or len(num1) > 0:
#     n1 = ord(num1.pop()) - ord('0') if len(num1) > 0 else 0
#     n2 = ord(num2.pop()) - ord('0') if len(num2) > 0 else 0
#
#     temp = n1 + n2 + carry
#     res.append(temp % 10)
#     carry = temp // 10
# if carry: res.append(carry)
# print(''.join([str(i) for i in res])[::-1])

# Decode the String
# import re
#
# class Solution:
#     def decodeString(self, s):
#         find_pat = re.compile(r'(\d+)\[(\w+)\]')
#
#         while find_pat.search(s):
#             mo = find_pat.search(s)
#             decoded_string = ''
#             decoded_string += (str(mo.group(2)) * (int((mo.group(1)))))
#
#             s = s.replace(mo.group(), decoded_string)
#
#         return s


# print(Solution().decodeString('2[abc]3[cd]ef'))
# Solution().decodeString('3[a]2[bc]')
# print(Solution().decodeString('3[a2[c]]'))
# Solution().decodeString('3[a]ef2[bc]')
# Solution().decodeString("3[a]2[bc]")


# """
# 4
# bcdef
# abcdefg
# bcde
# bcdef
# """

# from collections import OrderedDict
#
# get_num_of_words = int(input())
#
# word_order = []
# word_val = []
# word_dict = OrderedDict()
#
# for i in range(get_num_of_words):
#     line = input()
#     if line:
#         word_order.append(line)
#
#
# for word in word_order:
#
#     if word:
#         if word not in word_dict.keys():
#             word_dict[word] = 1
#
#         else:
#             word_dict[word] = word_dict[word] + 1
#
# print(len(word_dict.keys()))
# for word_val in word_dict.values():
#     print(word_val, end =" ")

# input_str = 'ffccddddee'
# alpha_count = {}
# max_value = 0
# reverse_order = ''
# sort_reverse_order = ''
# word_value_list = []
# for alpha in input_str:
#     if alpha not in alpha_count.keys():
#         alpha_count[alpha] = 1
#     else:
#         alpha_count[alpha] = alpha_count[alpha] + 1
#
#
# for key, value in alpha_count.items():
#     if value > max_value:
#         max_value = value
#         if value not in word_value_list:
#             reverse_order = key + reverse_order
#
#     else:
#         reverse_order += key
#
# for word in reverse_order[:3]:
#     if alpha_count[word] not in word_value_list:
#         sort_reverse_order += word
#     else:

# from collections import OrderedDict
#
#
# def word_occurrence(s):
#     alpha_count = OrderedDict()
#     max_value = 0
#     reverse_order = ''
#     for alpha in s:
#         if alpha not in alpha_count.keys():
#             alpha_count[alpha] = 1
#         else:
#             alpha_count[alpha] = alpha_count[alpha] + 1
#
#     for key, value in alpha_count.items():
#         if value > max_value:
#             max_value = value
#             reverse_order = key + reverse_order
#
#         else:
#             reverse_order += key
#
#     for char in reverse_order[:3]:
#         print(char, alpha_count[char])
#
#
# if __name__ == '__main__':
#     s = sorted('aabbbccde')
#     word_occurrence(s)
#
# from collections import Counter
#
# for c in Counter(sorted('ccbbbaade')).most_common(3):
#     print(c[0], c[1])


# def collatz(number):
#
#     if number == 1:
#         exit(0)
#
#     if number % 2 == 0:
#         print (number // 2)
#         collatz(number // 2)
#
#     else:
#         print (3*number + 1)
#         collatz(3*number + 1)
#
# collatz(int(input()))


# words = ["w","wo","wor","worl", "world"]

# words = ["t","ti","tig","tige","tiger","e","en","eng","engl","engli","englis","english","h","hi","his","hist","histo","histor","history"]
# words = ["k","lg","it","oidd","oid","oiddm","kfk","y","mw","kf","l", "l", "o","mwaqz","oi","ych","m","mwa"]
#
# words.sort()
# words_set, longest_word = set(['']), ''
# for word in words:
#     print(words_set)
#     # print(word[:-1])
#     if word[:-1] in words_set:
#         words_set.add(word)
#         if len(word) > len(longest_word):
#             longest_word = word
# print(longest_word)


# valid = set([""])
#
# for word in sorted(words, key=lambda x: len(x)):
#     if word[:-1] in valid:
#         valid.add(word)
#
# print(valid)
# print(sorted(valid))
# print(max(sorted(valid), key=lambda x: len(x)))


# longest_word = ''
# longest_word_list = []

# longest_word_length = 0

# words.sort()
# print(words)
# for word in words:
#     word_length = 0
#
#     for i in range(1, len(word)+1):
#         if word[:i] in words:
#             print(word[:i])
#             word_length += 1
#         else:
#             word_length = 0
#             break
#
#     if word_length > len(longest_word):
#         longest_word = word
#         longest_word_list.append(longest_word)
# print(longest_word_list)
# print(longest_word_list[-1])


from collections import OrderedDict
#
# pattern = "abba"
# str = "dog dog dog dog"
# str_list = str.split(" ")
#
# if len(set(zip(pattern, str_list))) == len(set(pattern)) \
#         and len(pattern) == len(str_list) \
#         and len(set(pattern)) == len(set(str_list)):
#     print(True)
# else:
#     print(False)

# EASY PROBLEMS

# SWAP CASE
# input wwW.HackER.com
# def swap_case(s):
#     l_s = list(s)
#     for i, char in enumerate(l_s):
#         if char.islower():
#             l_s[i] = char.upper()
#         elif char.isupper():
#             l_s[i] = char.lower()
#         else:
#             l_s[i] = char
#     return ''.join(l_s)
#
# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)


# SPLIT AND JOIN
#
# def split_and_join(line):
#     return '-'.join(line.split(" "))
#
#
# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

# input ABCDCDC
# input CDC

# Took the difference in length from string and substring


# import textwrap
#
# value = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
#
# string = textwrap.fill(text=value,width=4)
#
# print(string)

# import textwrap
#
# string = 'AABCAAADA'
# for substring in textwrap.wrap(text=string, width=3):
#     uniq = []
#     final_string = ''
#     for char in substring:
#         if char not in uniq:
#             uniq.append(char)
#             final_string += char
#     print(final_string)


# initial = 0
# get_split_count = int(len(string) // k)
# mod_list = []
# max = get_split_count
# for i in range(get_split_count):
#     mod_list.append(string[initial:(max - 1)])
#     initial += get_split_count
#     max += get_split_count


# PROBLEM

# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#
#
#     output = [[num_x, num_y, num_z] for num_x in range(x+1) for num_y in range(y+1) for num_z in range(z+1) if (num_x + num_y + num_z)!= n ]
#     print(output)


# PROBLEM
# https://www.hackerrank.com/challenges/nested-list/problem

# from collections import defaultdict
#
# if __name__ == '__main__':
#     student_grades = []
#     get_student = defaultdict(list)
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())
#         student_grades.append([name, score])
#
#     sorted_grades = sorted(student_grades, key=lambda value: value[1])
#
#     for grade in sorted_grades:
#         get_student[grade[1]].append(grade[0])
#
#     remove_least = min(get_student.items())[0]
#     del get_student[remove_least]
#
#     for student in sorted(min(get_student.items())[1]):
#         print(student)



#
# if __name__ == '__main__':
#     N = int(input())
#     print("\n")
#     complete_input = []
#     final_list = []
#     for _ in range(N):
#         s = input().split()
#         cmd = s[0]
#         args = s[1:]
#         if cmd != "print":
#             cmd += "(" + ','.join(args) + ")"
#             print(cmd)
#             print(type(eval("final_list." + cmd)))
#         else:
#             print(final_list)
#


# EXPERT PROBLEM
# https://www.hackerrank.com/challenges/how-many-substrings/problem

# def countSubstrings(s, queries):
#     sub_string_occurrences = []
#     for slice_elem in queries:
#         list_sub_string = []
#
#         if len(list(set(slice_elem))) > 1:
#
#             sub_string = s[slice_elem[0]:(slice_elem[1] + 1)]
#
#             for i in range(len(sub_string)):
#                 for j in range(i, len(sub_string) + 1):
#                     if sub_string[i:j] and sub_string[i:j] not in list_sub_string:
#                         list_sub_string.append(sub_string[i:j])
#
#             sub_string_occurrences.append(len(list_sub_string))
#
#         else:
#             sub_string_occurrences.append(1)
#
#     return sub_string_occurrences
#
#
# if __name__ == '__main__':
#
#     nq = input().split()
#
#     n = int(nq[0])
#
#     q = int(nq[1])
#
#     s = input()
#
#     queries = []
#
#     for _ in range(q):
#         queries.append(list(map(int, input().rstrip().split())))
#
#     result = countSubstrings(s, queries)
#     print(result)



# def is_leap(year):
#     leap = False
#     digit = [4, 100, 400]
#     leap = all([True if year % n == 0 else False for n in digit])
#
#     return leap
#
#
# year = int(input())
# print(is_leap(year))


# print(*range(1, int(input())+1), sep='')


# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
        # scores = list(map(float, line))
        # student_marks[name] = scores
    # query_name = input()
    # print(student_marks)
#
# if __name__ == '__main__':
#     n = int(input())
#     countries = set()
#     for _ in range(n):
#         country_name = input()
#         countries.add(country_name)
#
#     print(len(countries))


# if __name__ == '__main__':
#     n, m = input().split(" ")
#     array = input().split(" ")
#     set_a = set(input().split(" "))
#     set_b = set(input().split(" "))
#     print(set_a)
#     print(set_b)
#     print(array)
#     happiness = 0
#     for digit in array:
#         if digit in set_a:
#             happiness += 1
#         if digit in set_b:
#             happiness -= 1
#     print(happiness)

import re

# input_str = """11
# a = 1;
# b = input();
#
# if a + b > 0 && a - b < 0:
#     start()
# elif a*b > 10 || a/b < 1:
#     stop()
# print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides."""

# pat = re.compile(r'(\s&&\s)|(\s\|\|\s)')
# for line in input_str.split("\n"):
    # line = re.sub(r'(\s)?&&\s',' and ', line)
    # line = re.sub(r'(\s)?\|\|\s', ' or ', line)
    # print(line)

# line = 'n && && && && && &&n'
#
# line = re.sub(r'(\s)?&&(\s)',' and ', line)
#
# print(line)


# Python code demonstrate the working of
# sorted() with lambda

# Initializing list of dictionaries
# lis = {"Nandini": 20,"Manjeet": 21, "Nandine": 20}
# print(sorted(lis.items(), key=lambda i: i[0]))

# using sorted and lambda to print list sorted
# by age
# print(lis)
# "The list printed sorting by age: "
# print(sorted(lis.items(), key=lambda i: i[0]))

import re
#
# reg_pat = re.compile(r'')
#
# mo = reg_pat.search('abc_d@mail.com')
#
# print(mo.group())


# if __name__ == '__main__':
#     n = int(input())
#     lines = []
#     while True:
#         for i in range(n):
#             line = str(input())
#             lines.append(line.strip())
#         break
#
#     for element in lines:
#         reg_pat = re.match(r'<[a-z](\w|\.|-|_)+@([a-z]{2,10})\.([a-z]{1,3})>', element.split()[1])
#         if reg_pat:
#             print(element)


# import re
#
# s = "Testyou1234!"
#
# # if re.match(r'[A-Za-z0-9]{8,30}', s) and re.compile(r'(!|@|#|\$|%|\^|&|\*|\(|\)){1,}').findall(s):
# #     print("yes")
# # else:
# #     print("no")
#
# # s_char =
# # print(s_char.findall(s))
# # print(s_char)
#
# if re.match(r'[A-Za-z0-9@#$%^&+)=(]', s):
#     print("yes")
#
#

from itertools import combinations

# s = 'asvkugfiugsalddlasguifgukvsa'
# s = 'beabeefeab'
# s = 'muqqzbcjmyknwlmlcfqjujabwtekovkwsfjrwmswqfurtpahkdyqdttizqbkrsmfpxchbjrbvcunogcvragjxivasdykamtkinxpgasmwz'
#
#
# unique_list = []
# for char in s:
#     if s.count(char) >= 2 and char not in unique_list:
#         unique_list.append(char)
#
# get_pairs = []
# for i in range(len(unique_list)):
#     for j in range(i + 1, len(unique_list)):
#         get_pairs.append([unique_list[i], unique_list[j]])

# get_pairs = list(combinations(unique_list, 2))
#
# longest_words = []
# for pair in get_pairs:
#     final_string = s
#     remove_char = list(set(''.join(s)) - set(''.join(pair)))
#     for rm_char in remove_char:
#         final_string = final_string.replace(rm_char, '')
#     for select in range(1, len(final_string)):
#         if final_string[select - 1] != final_string[select]:
#             pass
#         else:
#             break
#
#     if select == len(final_string) - 1 and final_string[select - 1] != final_string[select]:
#         longest_words.append(final_string)

    # if (all([True if final_string[select - 1] != final_string[select] else False for select in
    #          range(1, len(final_string))])):
    #     longest_words.append(final_string)


# print(longest_words)
# if longest_words:
#     print(sorted(longest_words, key=len)[-1])
#     print(len(sorted(longest_words, key=len)[-1]))
