def decorator_1(func):
    def dec_1():
        return "<= " + func()
    return dec_1
def decorator_2(func):
    def dec_2():
        return func() + " =>"
    return dec_2
@decorator_1
@decorator_2
def hello_w():
    return "Hello world!"
print(hello_w())
