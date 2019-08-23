# lesser of 2 evens 

def myfunc(a,b):
    if a%2==0 and b%2==0:
        print (min(a,b))
    else:
        print(max(a,b))


myfunc(2,7)

# Animal Crackers
def animal(st):
    string = st.lower().split()
    print (string)
    first_word = string[0][0]
    second_word = string[1][0]
    if first_word == second_word:
        print ('True')
    else:
        print('False')

animal('KAnf  Crazy')

# Makes 20 
def makes (a,b):
    if a + b == 20:
        print('True')
    elif a==20 or b==20:
        print('True')
    else:
        print('False')

makes(20,10)

#blackjack
def black(a,b,c,):
    if sum((a,b,c)) <= 21 :
        print (sum((a,b,c)))
    elif (sum((a,b,c))-10) <= 21 and 11 in (a,b,c):
        print((sum((a,b,c))-10))
    else:
        print('BUST')

black(2,11,12)

#summer of 69
def summer(a):
    total  = 0
    add = True
    for i in a:
        while add:
            if i != 6:
                total = total + i
                break
            else:
                add=False
        while not add:
            if i != 9:
                break
            else:
                add = True
                break
        print(total)

summer([1,6,9])

#spygame

def spygame(nums):
    check = [0,0,7]
    for i in nums:
        if i == check[0]:
            check.pop()
        else:
            print(i)


spygame([0,0,7,2,3,4])



            

Given an array containing positive and negative integers, return the sum of the subarray with the maximum sum.

 

# [ 1, -2, 3, 4, -5, 6 ] => 8
# [3, 4, -5, 6] (beginning and end of the subarray with maximum sum)
 