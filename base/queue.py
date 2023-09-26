from collections import deque

# 创建一个新的空队列
queue = deque()

# 入队
queue.append("task 1")
queue.append("task 2")
queue.append("task 3")
print(queue)  # 输出: deque(['task 1', 'task 2', 'task 3'])

# 出队
task = queue.popleft()  # 从队列左边弹出一个元素
print(task)  # 输出: task 1
print(queue)  # 输出: deque(['task 2', 'task 3'])

task = queue.pop()
print(task)  # 输出: task 3
print(queue)  # 输出: deque(['task 2'])
