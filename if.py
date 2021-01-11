score = float(input('score = '))
if score >= 90:
  if score >= 95:
    print('非常优秀')
  else:
    print('优秀')
elif score >= 80 :
  print('良')
elif score >= 60 :
  print('及格')
else:
  print('差')



# 判断是否可以构成三角形
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a+b > c and a + c > b and b + c > a :
  print('可以')
else:
  print('不可以')
  