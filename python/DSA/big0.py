import time 
startTime = time.time()

def count_add(n):
    final = 0
    for i in range(n+1):
        # final = final + i
        final += i
    print (final)
    print ('The script took {0} second !'.format(time.time() - startTime))

count_add(10)


lst = [1,2,3,4]

dic = dict(lst)
print(dic)

# Growth is linear with input -Constant O(0)
def constant(n):
    print (n)

constant(lst)

# gowth is up with minimal inputs - Linear clear

def quadrant(n):
    for i in n:
        print(i)

quadrant(lst)

# gowth is exponential with minimal input  - Exponential
def log(n):
    for x in n:
        for y in n:
            print (x,y)

log(lst)

# n + n - Insignificant  O(n) 
def print_2(n):
    for i in n:
        print(i)
    for i in n:
        print(i)

print_2(lst)