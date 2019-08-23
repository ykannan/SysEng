x = -7
while x < 10:
    x = x+1
    print ('This is the value of {v}'.format(v=x)) 
else:
    print('The value is greater than 10 and it is {v}'.format(v=x))

# using break, contiue and pass conditions


# PASS Condition --> passes the condition
x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    #print ('the number is {numb}'.format(numb = i))
    pass
print ('end of code')

# CONTINUE Condition -- > goes to the closest enclosing loop 
x = [1,2,3,4,5,6,7,8,9,10]
for i in x:
    if i == 4:
        continue
    print ('the number is {numb}'.format(numb = i))

# BREAK Condition -- > breaks the existitng loop if the condition is met 
x = [11,12,13,14,15,16,17,18,19,20]
for i in x:
    if i == 17:
        break
    print ('the number is {numb}'.format(numb = i))