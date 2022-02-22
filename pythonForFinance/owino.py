def applt_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5


print(applt_twice(add_five, 10))