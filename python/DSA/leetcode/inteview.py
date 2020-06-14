# # find the frequency of the substring in the main string
# String = "OrangesforApplesforApplesforApplesforApplesforApplesforOranges"
# Substring = "ApplesforApples"

count = 0

for i in range(len(String) - len(Substring)):
  if String[i:(len(Substring) + i)] == Substring:
    count += 1
    print("Original String: {}".format(String[i:(len(Substring) + i)]))
    print("Substring {}".format(Substring))
    print("Count = {}".format(str(count)))

print("Count = {}".format(str(count)))



# # string = """
# # continuous-api-1.hf-dev.net
# # continuous-api-2.hf-dev.net
# # continuous-web-2.hf-dev.net
# # """

# # # print the number of the host roles like the above example
# # # api roles are 2 and web roles are 1
# # # output is
# # # api 2
# # # web 1

# # print(string.split())
# count = 0
# for i in range(len(String) - len(Substring)):
#   if String[i:len(Substring) + i] == Substring:
#     count += 1

# print(count)








# # Bash
# # How would you write a shell script that prints all the additional arguments passed to it in reverse order?
# # ./script.sh one two three four five six

# # Five 
# # Four
# # Three
# # Two
# # One
# for i in "$@"; do
#   echo "$i"
# done | tac


# # Python
# # Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# # between min and max (both included) values provided as program command line parameters.
# # The numbers obtained should be printed in a comma-separated sequence on a single line.

def operation(min,max):
  r = range(min,max)
  tmp = []
  for x in r:
    if x%7 ==0 and x%5!=0:
      tmp.append(x)
  print(tmp)

operation(0,100)