# 创建一个新的空堆栈
stack = []

# 压栈 (push)
stack.append("item 1")
stack.append("item 2")
stack.append("item 3")
print(stack)  # 输出: ['item 1', 'item 2', 'item 3']

# 出栈 (pop)
item = stack.pop()
print(item)  # 输出: item 3
print(stack)  # 输出: ['item 1', 'item 2']
