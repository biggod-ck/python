# 在Python中构造循环结构有两种做法，一种是for-in循环，一种是while循环

sum = 0
for x in range(101):
  sum += x
print(sum)

print(range(3))
# range 包含开始 不包含结束
# range(101) 0 - 100
# range(10,101) 10 - 100
# range(1,101,2) 1 - 100 步长为2 1 3 5
# range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的
sum2 = 0
for y in range(0,101,2):
  sum2 += y
print(sum2)

sum3 = 0
for z in range(0,101):
  if z % 2 == 0:
    sum3 += z
print(sum3)

import random
answer = random.randint(1,100)
print('answer',answer)
counter = 0
while True:
  counter += 1
  number = int(input('请输入: '))
  if number < answer:
    print('大一点')
  elif number > answer:
    print('小一点')
  else:
    print('终于猜对了')
    break
print('总共猜了%d次' % counter)
if counter > 7 :
  print('你的额智商不行呀')

for i in range(1,10):
  for j in range(1,10):
      print('%d*%d=%d' % (i, j, i * j), end='\t')
    