#  *args = returns tuples for multiple inputs (1,2,3,4,5,6)
# **kwags = returns dictonary for multiple inputs (fruit=2.00, veggie=1.25)

#args
def myfunc(*args):
    print(args)
    addition = sum(args)
    return addition 
eg = myfunc(1,2,3,4,5,6)
print (eg)

#kwargs
def myfunc2(**kwargs):
    print (kwargs)
    if 'fruit' in kwargs:
        print ('This fruit costs {c}'.format(c=(kwargs['fruit'])))
    else:
        print('No fruit')

myfunc2(fruit=2.00, veggie=1.25)

# #args + kwargs
# def myfunc3(*args,**kwargs):
#     print(*args,**kwargs)
#     print ('{} is my favourite dish, and it costs {}'.format(args[0],kwargs['veggie']))
# myfunc3(10,11,veggie='ehhs' )



def myfuncx(s):
    result = ""
    index = 0
    for x in s:
        if index%2== 0:
            result += x.lower()
        elif index%3== 0:
            result += x.upper()
        else:
            pass
        index=index+1
    print(result)

myfuncx('anthropomorphism')



def myfunc6(*args):
    lst =[]
    for x in args:
        if x%2 ==0:
            lst.append(x)
        else:
            pass
    return (lst)

myfunc6(5,6,7,8)


    