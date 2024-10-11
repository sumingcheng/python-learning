# 整数类型
integer_example = 42

# 浮点数类型
float_example = 3.14159

# 复数类型
complex_example = 1 + 2j

# 字符串类型
string_example = "Hello, Python!"

# 列表类型 列表（List）有序、可变、
# 列表是一个有序且可变的集合。你可以添加、删除或修改列表中的元素。它很像数组，但与传统的数组相比，Python 的列表更加灵活，因为它可以存储不同类型的对象。
list_example = [1, 2, 3, 4, 5]

# 元组类型 元组（Tuple） 有序、不可变
# 元组与列表非常相似，都是有序的集合，但元组是不可变的。这意味着一旦创建了元组，你就不能更改其内容。这种不可变性使得元组可以用作某些场合下的字典键（其中要求键必须是不可变类型）
tuple_example = (1, 2, 3, 4, 5)

# 集合类型 集合（Set） 无序、不重复
# 集合是一个无序的集合类型，它不允许重复的元素。集合主要用于去重以及执行数学上的集合运算如并集、交集、差集等。集合中的元素也必须是不可变的类型。
set_example = {1, 2, 3, 4, 5}

# 字典类型 字典（Dictionary） 无序、键值对
# 字典在 Python 中类似于其他语言中的哈希表或映射（Map）。字典存储键值对，其中键必须是不可变类型，值可以是任何类型。字典的主要优点是提供了非常快的查找速度。
dict_example = {'name': 'John', 'age': 30, 'city': 'New York'}

# 你可以通过键来访问字典中的值
person = {
    "name": "Alice",
    "age": 30,
    "occupation": "Engineer"
}

print(person["name"])  # 输出: Alice

# 布尔类型
boolean_true = True
boolean_false = False


# 函数
def print_data_type(variable):
    print(f"Value: {variable}, Type: {type(variable)}")


# 打印各类型的值和类型信息
print_data_type(integer_example)
print_data_type(float_example)
print_data_type(complex_example)
print_data_type(string_example)
print_data_type(list_example)
print_data_type(tuple_example)
print_data_type(set_example)
print_data_type(dict_example)
print_data_type(boolean_true)
print_data_type(boolean_false)

'''
类定义 (class 关键字)：确实，class 关键字用于定义一个类。在例子中，Person 是类的名称。

初始化方法 (__init__ 方法)：
这是一个特殊的方法，用于类的初始化（构造函数）。每当创建类的新实例时，__init__ 方法都会自动执行。
__init__ 方法通常用于初始化实例属性，也就是说，它为每个新创建的实例设置初始状态。
self 参数是对当前类实例的引用，确保属性和方法被正确地绑定到具体的对象上。

方法 (introduce 方法)：
这是类定义的一个方法，需要显式调用才会执行。它不像 __init__ 那样自动执行。
introduce 方法使用 self 来访问和操作实例的属性（例如，self.name, self.age 等）。

self 关键字：
在类的方法中，self 表示类的当前实例。这是一种向方法传递实例本身的方式。
使用 self 可以确保你可以在类的各个方法中自由访问实例属性和其他方法。
创建实例：

当你使用 Person 类创建一个新的对象（实例）时，你会调用类名后跟圆括号，并传入初始化方法 __init__ 需要的参数。
创建实例时传入的参数会通过 __init__ 方法传递给 self 属性，从而在新对象上设置这些属性。
'''


class Person:
    def __init__(self, name, age, occupation):
        self.name = name  # 姓名属性
        self.age = age  # 年龄属性
        self.occupation = occupation  # 职业属性

    def introduce(self):
        # 一个简单的方法，用来介绍这个人
        print(f"Hello, my name is {self.name}. I am {self.age} years old and I am a {self.occupation}.")


"""
创建 Person 类的实例时，传入 name, age, occupation 作为参数。
这些参数在 __init__ 方法中被接收，并将它们分别赋值给 self.name, self.age, 和 self.occupation。
当调用 introduce 方法时，它使用这些已经设置好的属性来打印个人信息。
"""
person1 = Person("Alice", 30, "Engineer")

# 调用方法
person1.introduce()  # 输出: Hello, my name is Alice. I am 30 years old and I am a Engineer.
