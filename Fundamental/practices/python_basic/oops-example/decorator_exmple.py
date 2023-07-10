from time import time


def performance(fun):
    def wrapper_fun(*arg, **kwargs):
        t1 = time()
        response = fun(*arg, **kwargs)
        t2 = time()
        print(f'took {t2 - t1} s')
        return response

    return wrapper_fun


@performance
def long_time():
    for i in range(100000000):
        i * 5


long_time()
