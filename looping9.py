a = b = c = 1
for i in range(9):
    print(c, end=" ")
    if (i >=1) :
        c = a+b
    a = b
    b = c

print("\n================\n")
a = b = 1
for i in range(9):
    print(a, end=" ")
    a = b
    b = c