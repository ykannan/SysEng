#Sample Dictionary : {0: 10, 1: 20}
#Expected Result : {0: 10, 1: 20, 2: 30}

dic = {
  0:10,
  1:20
}

dic[2]=30
print(dic)


d = {0:10, 1:20}
print(d)
d.update({2:30})
print(d)