# reverse of the string should be same as the normal string
x = "race a car"

y = x.replace(" ","" ).lower()
y1 = y.replace(",","" ).lower()
y2 = y1.replace(":","" ).lower()
if y2 == y2[::-1]:
  print("True")
else:
  print("False")