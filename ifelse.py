#条件判断
age = 20
if age >= 18:
	print("your age is " ,age)
	print("adult")

#条件判断
age = 3
if age >= 18:
	print('your age is', age)
	print('adult')
else:
	print('your age is', age)
	print('teenager')

#加上输入
birth = input('birth:')
birth = int(birth)
if birth < 2000:
	print("00前")
else:
	print('00后')
	
s = input('birth:')
birth = int(s)
if birth < 2000:
	print("00前")
else:
	print('00后')
