def non_repeating(strg):
    counter = {}
    for i in strg:
        if i in counter:
            counter[i] += 1
            print(counter)
        else: 
            counter[i] = 1
    for i in counter:
        if counter[i] == 1:
            print(i)

non_repeating('oaabrbccdecdf')