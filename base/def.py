# def greet(name="World"):
#     return "Hello, " + name + "!"
#
#
# # 调用函数
# print(greet())  # 输出: Hello, World!
# print(greet("Alice"))  # 输出: Hello, Alice!


# def make_pizza(size, *args):
#     return f"Making a {size}-inch pizza with the following toppings: {', '.join(args)}."
#
#
# print(make_pizza(12, "pepperoni", "mushrooms", "green peppers"))  # 输出相关的pizza信息


# def build_profile(first, last, **user_info):
#     user_info["first_name"] = first
#     user_info["last_name"] = last
#     return user_info
#
#
# profile = build_profile("Albert", "Einstein", location="Princeton", field="physics")
# print(profile)

# pairs = [(1, 3), (2, 2), (4, 1)]
# sorted_pairs = sorted(pairs, key=lambda pair: pair[1])
# print(sorted_pairs)  # 输出：[(4, 1), (2, 2), (1, 3)]

# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x**2, nums))
# print(squared)  # 输出：[1, 4, 9, 16]


