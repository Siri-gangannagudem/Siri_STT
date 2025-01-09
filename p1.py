def f(a, b):
    if(a < 0):
        return 0
    elif (b < 0):
        return 0
    elif (a%2 == 0 and b%2 == 0):
        return a + b
    elif (a%2 == 0 and b%2 != 0):
        return a - b
    elif (a%2 != 0 and b%2 == 0):
        return a*b
    elif (a%2 != 0 and b%2 != 0):
        return a/b
    else:
        return -1

def g(a, b):
    if (a < 0):
        return 0
    elif (b < 0):
        return 0
    else:
        s = 0
        for i in range((a+b)%2):
            s += i
        return s

a = int(input())
b = int(input())
c = f(a, b)
d = g(a, b)
print(c)
print(d)   