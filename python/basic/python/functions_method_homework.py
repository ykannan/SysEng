#1
def vol(r):
    volume = (r*1.33*3.14)*(r**2*r)
    print (volume)

vol(2)

#range check 
def range1(num,low,high):
    if num in range(low,high):
        print('withing range')
    else:
        print('out of range')

range1(3,20,10)


#count upeer and lower char
def char(s):
    d = {'Upper': 0,
         'lower': 0
    }
    for c in s:
        if c.isupper():
            d['Upper']+=1
        elif c.islower():
            d['lower']+=1
        else:
            print('None')
    print(d)

char('This is a funny guuuuuuuGy')

# palindrome
def palindrome(string):
    r = string[::-1]
    if r == string:
        print(r)
        print('True')
    else:
        print(r)
        print('flase')

palindrome('nurses run')

#unique list
def unique(mylist):
    new = set(mylist)
    unique_list = list(new)
    print (unique_list)

unique([1,1,1,1,2,2,2,3,4,4,4,5])

#multiply all the numbers in a list
def mul(mylist):
    total = mylist[0]
    for i in mylist:
        total *= i 
    print (total)

mul([1,1,1,1])

#
import string
def panogram(string, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    print(alphaset)

panogram ('a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z')
    