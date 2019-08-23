list_1 = [1,2,3,'four',5.21] # list can contain strings, integers and floats
list_2 = [6,7,8,9]
new_list_1 = list_1 + list_2 #adding two lists
new_list_1.append('10') # appending a value to the end of an exisitng list, since lists are mutable
print (new_list_1)
x = new_list_1.pop(-2) # removes value from the list, depends on reverse indexing
print ('The popped value {result}'.format(result= x)) # using string formatting


for i in range(len(new_list_1)):
    print (new_list_1[i])



x = [100,5,60,1,300,45]
y = [100,5,60,1,300,45]
x.sort()        # sorting the list, valid ony for integers  
y.reverse()     # reversing the list, valid ony for integers 
print(x) 
print(y)