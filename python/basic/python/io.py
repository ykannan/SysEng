# file = open(r'C:\\Users\\Yogesh\\Desktop\\python\\test.txt', "w") # old way of doing it, python will throw error if someone is tryiing to work with it 
with open('C:\\Users\\Yogesh\\Desktop\\python\\test.txt', "a") as file:
    file.write('new file  hello this is a single strein gthat we dont like')
file.close()

with open('C:\\Users\\Yogesh\\Desktop\\python\\test.txt', "r") as file:
    x = file.read()         # prints everything in as a string
    file.seek(0)            # resets the cursor back to 0 suck that it doesn't return empty value
    y = file.readlines()    # prints everything like a list for looping 
    print(x)
    print (y)
file.close()


# mode 
# r --> read only , 
# r+ --> read + write, overwites at the top of the line 
# w --> wirte only,
# w+ --> write + read, overwrites existing files
# a --> append only