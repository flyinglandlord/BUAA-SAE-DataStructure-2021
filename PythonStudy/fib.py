n = int(input('请输入要一个整数：'))
n_2 = 0
n_1 = 1
current = 1
for x in range(2, n+1):
  current = n_2 + n_1
  n_2 = n_1
  n_1 = current
print('第%d个数是%d'%(n, current//(2**32-1)))