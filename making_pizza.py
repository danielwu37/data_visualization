#导入整个模块
import pizza
pizza.make_pizza(15, "pepperoni")
pizza.make_pizza(11, "mushrooms", "green peppers")
pizza.make_pizza(19, "extra cheess")

#另一种写法
from pizza import make_pizza
make_pizza(12, "green peppers")
make_pizza(22, "mushrooms", "extra cheese")

#使用别名来缩写
from pizza import make_pizza as t
t(12, "pepperoni", "green peppers")
t(22, "mushrooms", "extra cheese")
