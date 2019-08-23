#MAp Function
def square(x):
    return x**2
my_list = [1,2,3,4,5]
for i in map(square,my_list):
    print(i)

#Example 2
def splicer(mystring):
    if len(mystring)%2==0:
        print('Even')
    else:
        print((mystring)[0])

    
names = ['Andy', 'Eve', 'Sally']
list(map(splicer,names))

#lambda function
print(list(map(lambda x : x**2, my_list)))
