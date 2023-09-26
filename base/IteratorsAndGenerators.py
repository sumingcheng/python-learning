# my_list = [1, 2, 3]
# my_iter = iter(my_list)
#
# print(next(my_iter))  # 1
# print(next(my_iter))  # 2


def my_gen():
    yield 1
    yield 2
    yield 3


gen = my_gen()
#
print(next(gen))  # 1
print(next(gen))  # 2
