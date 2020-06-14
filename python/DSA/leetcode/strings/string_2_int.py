r = '42'
print(int(r))


# extract digist into integers
x = "4193 with words"
y = x.split()

for i in y:
  if i.isdigit():
    print(int(i))