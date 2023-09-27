class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")


class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# self 是一个指向类实例的引用，它允许我们访问类的属性和方法。
# 创建一个 Animal 实例（这通常不太有意义，因为 Animal 类是为子类提供基础的）
generic_animal = Animal("Generic")
# 此行会抛出错误，因为 Animal 类的 speak 方法并没有实现
# print(generic_animal.speak())

# 创建一个 Dog 实例
buddy = Dog("Buddy")
print(buddy.speak())  # 输出: Buddy says Woof!
