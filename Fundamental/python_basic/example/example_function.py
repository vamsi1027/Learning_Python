# TODO function, Parameters, Argument, default, return, method vs function

# Case 1
def get_city():
    print("City name is Hyd")
get_city()

# Case 2
def get_name(name):
    return name
print(get_name("vamsi"))

# Case 3:
def get_name(name="harish"):
    print(name)
get_name()

# Case 4:
def arg_vs_paramter(first, last):
    print(first, last)
arg_vs_paramter(last='koka', first='vamsi')

# Case 5:
def sub(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)
print(sub(2, 4))

# Case 6:
def credit_bile(name_of_the_ac):
    print(f"Hey, This is mine credit card {name_of_the_ac}")
credit_bile("vamsi")