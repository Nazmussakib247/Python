#While loop ----> execute a set of command as long as a condition is true
i = 1
while i < 6 :
    print(i)
    i += 1

#The break Statement (Stop loop even though condition is true)
i = 1
while i < 6 :
    print(i)
    if i == 3 :
        break
    i += 1

#Continue statement (Stop current iteration and continue with next)
i = 1
while i < 6 :
    i += 1
    if i == 4 :
        continue
    print(i)

#The else Statement
i = 0
while i < 10 :
    i += 1
    print(i)
else:
    print("i is no longer valid")