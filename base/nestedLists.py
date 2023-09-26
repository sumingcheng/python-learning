# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transposed = [[row[i] for row in matrix] for i in range(3)]
# print(transposed)  # 输出: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

evens = [x for sublist in nested_list for x in sublist if x % 2 == 0]
print(evens)  # 输出: [2, 4, 6, 8]
