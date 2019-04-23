#直接输入文本
print('hello python world!')

#变量
hello = ('hello python world!')
print(hello)

#大小写
hello = ('hello world!')
print(hello.title())

#制表符,换行
print("my favorite food are following:\n\tpork\n\tbeef\n\tfish")

#连接字符串
question = ("where are you?")
answer = ("I am home.")
print(question.title() + "\n" + answer)
#用逗号连接多个字符串
print("where are you?" , "I am home." , "Got it.")

#计算
print("2 + 3 = ", 2 + 3)

#首字母大写，全部大写，全部小写
name = ("daNiel")
print(name + "首字母大写的结果是" + name.title())
print(name + "全部大写的结果是" + name.upper())
print(name + "全部小写的结果是" + name.lower())
