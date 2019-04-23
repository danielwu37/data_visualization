#输入
name = input("请输入你的名字:")
print("hello," + name + "\n\tWelcome to python world!")

#小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
s1 = 72
s2 = 85
result = s2-s1
result = result/s1*100
name = "小明"
print('%s成绩提高了%.1f%%' %(name,result))

s1 = 72
s2 = 85
result = s2-s1
result = result/s1*100
print('小明成绩提高了%.1f%%' %result)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1485926)

#数字转字符
age = 23
print("祝你" + str(age) + "岁生日快乐")

