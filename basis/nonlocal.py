def outer():
    x = 10  # 外部函数的变量

    def inner():
        nonlocal x  # 声明 x 是非局部变量
        x = 20  # 修改外部函数的变量 x

    inner()
    print(x)  # 输出 20，因为 inner 函数修改了 x 的值


outer()
