def f4(a):
    global c
    c = 10
    print("c de f4:", c)
    print(a + x + c)

x = 4
c = -1
f4(1)
print("c global:", c)