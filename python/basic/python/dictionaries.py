dict = { 
'apple' : 1.25,
'ball'  : 2.00,
'cat'   : 'nine',
'dog'   : [0,0,10]
}
# can contain an integer, list , float, string
# dict cannot be sorted

print (dict['apple'])
print (dict['dog'])
print (dict['dog'][2])      # can retrieve an index from a list in dict 
print ('There are {x} people in a row'.format(x = dict['dog'][2])) # using dict + list values in a string 

dict['dog'][1] = 1000       # dict are mutable, overriding
print (dict['dog'])

dict['elephant'] = 'huge'   # adding new key:value to existing dict
print (dict.keys())         # to prnt all the Keys pairs
print (dict.values())       # to prnt all the Values pairs
print (dict.items())        # to prnt all the Key:Value pairs