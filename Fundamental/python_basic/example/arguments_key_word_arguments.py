# TODO: *arg **kwarg

# TODO: *arg --> list, set, tuple, dictionary
def arguments_case1(*arg):
    print(f"Hey, this is my arg {arg}")


arguments_case1({"id": 1, "name": "vamsi"})


def super_function(*arg, **kwarg):
    total = 0
    for iteam in kwarg.values():
        total += iteam
    return sum(arg) + total


print(super_function(1, 2, 3, 4, num1=2, num2=3))
