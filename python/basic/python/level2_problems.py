def as_33(mylist):
    print(len(mylist))
    for i in range(0,len(mylist)-1):
        if mylist[i] == 3 and mylist[i+1] == 3:
            print ('True')
        else:
            print('False')

as_33([1,3,1])

def as_332(mylist):
    print(len(mylist))
    for i in range(0,len(mylist)-1):
        if mylist[i:i+2] == [3,3]:
            print ('True')
        else:
            print('False')

as_332([1,3,1])

#PAPER DOLL

def paper(test):
    result = ''
    for x in test:
        result += x*3
    print (result)

paper("holla")
    
