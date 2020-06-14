# anagram - the characters used in the string should be the same in count as of the real string
s = "anagram"
t = "nagaram"

ls = list(s)
sls = ls.sort()
ls2 = list(t)
sls2 = ls2.sort()

if sls == sls2:
  print("True")