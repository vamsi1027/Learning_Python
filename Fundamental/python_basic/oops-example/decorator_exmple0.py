def my_decorator(fun):
    def wrapper_func():
        print("**********")
        fun()
        print("**********")

    return wrapper_func


def hello(gree):
    print(f'hello, I m okay with {gree}')


hello("vampire")
