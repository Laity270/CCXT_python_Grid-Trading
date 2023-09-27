# try 和 except 是 Python 中用于异常处理的关键字。它们允许您编写代码来处理可能引发异常的情况，从而增加程序的稳定性和容错性。

# 以下是 try 和 except 的基本用法：
try:
    # 可能引发异常的代码块
    result = 10 / 0  # 试图除以零会引发 ZeroDivisionError 异常
except ZeroDivisionError as e:
    # 处理异常的代码块
    print("发生异常:", e)
    result = None  # 可以执行一些容错操作，如设置默认值

'''
在上面的示例中，try 块中包含了一段可能引发异常的代码，即试图除以零。如果在 try 块中的代码引发了异常，
Python 将立即跳转到与异常类型匹配的 except 块。在这里，我们捕获了 ZeroDivisionError 异常，并在
except 块中处理它，输出错误消息并执行容错操作。
'''

# 您可以使用多个 except 块来捕获不同类型的异常，以便更精确地处理它们。例如：
try:
    # 可能引发异常的代码块
    result = 10 / 0  # 试图除以零会引发 ZeroDivisionError 异常
except ZeroDivisionError as e:
    # 处理 ZeroDivisionError 异常
    print("发生 ZeroDivisionError 异常:", e)
except ValueError as e:
    # 处理其他异常类型，如 ValueError
    print("发生其他异常:", e)


