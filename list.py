#列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

#列表中第几个值
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates[3].title())

#列表中第几个值
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates[-1].title())

#引用列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
message = "my name is " + classmates[-2]+"."
print(message)

#修改列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

classmates[0] = ("Chris")
print(classmates)

#删除列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

del classmates[0]
print(classmates)

#末尾增加列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

classmates.append("jesse")
print(classmates)

#创建列表
classmates = []
classmates.append("tongqi")
classmates.append("jiejie")
print(classmates)

#插入列表
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

classmates.insert(2,"haoren")
print(classmates)

#删除列表末尾的元素并引用它
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print(classmates)

latest_classmate = classmates.pop()
print(classmates)
print(latest_classmate.title() + " is the final student.")

#删除列表第几个元素并引用它
classmates = ["xiaoming","xiaoli","Daniel","andy"]
print("I have 4 classmates, whose names are followings: " , classmates)

second_classmate = classmates.pop(1)
print(second_classmate.title() + " has dropped out of school.")
print("so I only have 3 classmates now, whose names are:", classmates)
