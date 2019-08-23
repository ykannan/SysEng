def name_function_one():
    """
    DOCSTRING: Information abou the function
    INPUT: No input 
    OUTPUT: Hello
    """
    print('hello')

name_function_one()


#######
def say_hello(name_1='NAME'):       # saves output variable
    print('hello ' +name_1)

say_hello('Yogesh')
# print(x)

##########
def addition(a,b):
    return (a+b)

r = addition(7,10)
print(r)

############
# find word dog in a string
def find(string):
    if 'dog' in string.lower():
        return True
    else:
        return False
res = find('My Dog ran away too far')
print(res)

#or
def find(string):
    return 'dog' in string.lower()                 # x in x = boolean

res = find('My Dog ran away too far')
print(res)


# pig latin
def pig(word):
    first_letter= word[0]
    if first_letter in 'aeiou':
        pig_word = word + 'ay'
    else:
        pig_word = word[1:] + first_letter + 'ay'
    return pig_word

result = pig('apple')

print(result)


######
# input T or F 
def myfunc(s):
    if s == True:
        return 'Hello'
    elif s == False:
        return 'Goodbye'
        
c = myfunc(False)
print (c)

####
def myfunc(x,y,z):
    if z == True:
        return x
    else:
        return y

t = myfunc(True, 'ranfdom',False)
print(t)