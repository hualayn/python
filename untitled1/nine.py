a = []
for i in range(1,10):
    b = ''
    for ii in range(1,i+1):
        b = b + str(i) + " * " + str(ii) + " = " + str(ii*i) + " | "
    a.append(b)
for a in a:
    print(a)