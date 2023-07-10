# Interable
# Iterator
# Generators

def generator(num):
    for i in range(num):
        yield i


for iteam in generator(100000000):
    print(iteam)


# obj = generator(5)

# try:
#  print(next(obj))
#  print(next(obj))
# print(next(obj))
# except:
#   print("Sorry, I can not able to do it")
#   print("doing good")
# finally:
#   print("always will execute")


def testing_generator(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


response = testing_generator(100000000)
print(response)
