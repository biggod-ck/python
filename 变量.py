a = 100
b = 12.345
c = 1 + 5j
d = 'hello, world'
e = True

print(type(a))    # <class 'int'>
print(type(b))    # <class 'float'>
print(type(c))    # <class 'complex'>
print(type(d))    # <class 'str'>
print(type(e))    # <class 'bool'>

a1 = int('123')
print(a)
a2 =float('1')
print(a2)
a3 = str('123aasd')
print(a3)

flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
flag4 = flag1 or flag2
flag5 = not(1 != 2)

print(flag0,flag1,flag2,flag3,flag4,flag5)

bool1 = True
bool2 = False

print(bool1 and bool2,bool1 or bool2)

