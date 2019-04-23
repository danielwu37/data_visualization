#循环
names = ['daniel','candy', 'andy']
for name in names:
	print(name.title() + " is my friend.")

#列举
sum = 0
for x in range(10):
	sum = sum + x
print("\n\t", sum)

#不断循环
sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2
print(sum)

#提前结束循环
n = 1
while n <=100:
	if n > 10:
		break
	n = n +1
	print(n)
print('END')

#跳过循环
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0: # %表示相除的余数
		continue   #continue语句会直接继续下一轮循环，后续的print()语句不会执行
	print(n)
