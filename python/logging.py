# cat /var/log/nginx/access.log | grep https://* | awk '{print $1}' |  sort -n | uniq -c | | head -n 15


import re
from collections import Counter

regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
file_open = open("/Users/yogeshkannan/Desktop/SysEng/python/logs.txt")
file_read= file_open.read()
my_iplist = re.findall(regex, file_read)
ip_count = Counter(my_iplist)
print(ip_count)

for x,y in ip_count.items():
    print(x,y)

# import re
# from collections import Counter

# f_open = open("/Users/yogeshkannan/Desktop/SysEng/python/logs.txt")
# f_read = f_open.readlines()
# my_list = []
# for i in f_read:
#     my_list.append(i)

# print(my_list)