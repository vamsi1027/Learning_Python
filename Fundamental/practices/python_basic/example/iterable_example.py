# TODO Iterable : list, dictionary, tuple, set,string

user_data = {
    "name": "vamsi",
    "age": 29,
    "address": "nbl"
}
for key,value in user_data.items():
    print(key, value)
for key in user_data.keys():
    print(key)
for values in user_data.values():
    print(values)