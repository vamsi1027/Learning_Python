def perform(func):
    print("hey func")

    def wrap_func(*args, **kwargs):
        func(*args, **kwargs)
        print("I'm a function from performance")
    print('Are you sure you want to')
    return wrap_func


@perform
def hello(greeting, emoji=':('):
    pass
    #print(greeting, emoji)


hello('hello world')
