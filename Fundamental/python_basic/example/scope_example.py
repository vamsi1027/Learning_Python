# TODO : scope example

# TODO : start with local
# TODO : Parent local
# TODO : Global
# TODO : build in python functions

if True:
    x = 10


def scope_example():
    x = 12
    print("value of scope")
    return x


print(x)
print(scope_example())

total = 0
def global_scop():
    global total
    total += 1
    return total

print(global_scop())

# Case 4
total_1 = 0
def global_count(total):
    total += 1
    return total
print(global_count(global_count(1)))

# TODO Case 6 Non-local example
def outer():
    x = "local"
    def inner():
        #nonlocal x
        x = "nonlocal"
        print("inner :", x)
    inner()
    print("outer:", x)

outer()